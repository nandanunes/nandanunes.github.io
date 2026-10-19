#!/usr/bin/env python3
"""
Static site builder: Notion export (Markdown & CSV) -> GitHub Pages site.

Usage:
    python3 build.py "path/to/Notion export folder" [output_folder]

The export folder is the one that contains "Fernanda Nunes <hash>.md" and the
"Fernanda Nunes" subfolder. Output defaults to ./dist.
"""
import hashlib, html, re, shutil, subprocess, sys, unicodedata, urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from markdown_it import MarkdownIt
from PIL import Image

# ----------------------------------------------------------------------------
# 1. SITE SETTINGS (edit these)
# ----------------------------------------------------------------------------
SITE = dict(
    name="Fernanda Nunes",
    year=2026,
    email_user="fernandauxd",
    email_domain="gmail.com",
    linkedin="https://www.linkedin.com/in/nandanunes/",
    resume="https://drive.google.com/file/d/1mO7QeL9CcewzPtvN9S1A8K9pUqX5HWLB/view?usp=sharing",
    intro_html=("Hello! I’m an interdisciplinary designer, currently working full-time at "
                '<a href="https://www.rovio.com/" target="_blank" rel="noopener">Rovio</a> '
                "as a Senior Game UX Designer."),
)

# Order = order on the site. Titles must match the Notion page titles.
# size: L (large card), M (medium card). Only used on the home page.
WORK = [
    ("Angry Birds Friends", "L"),
    ("Suspects", "L"),
    ("Tennis Clash – Social", "M"),
    ("AFK Football", "M"),
    ("Corpcity", "M"),
    ("Customer Segmentation", "L"),
    ("POS – Guerrilla", "L"),
]
SIDE = [
    "Crush Hour: A GameJam Project",
    "Política de Drogas é uma Questão de Mulheres",
    "COUP: Dinosaurs and 2nd WW Ed",
    "Alien Cable",
    "Women in History",
    "Nasty Island",
    "Fact Fuse",
    "Emperor of Quesin",
    "Sampa Stories",
    "Ela (She)",
    "Memo",
    "Super Button Mash",
]
# Case studies that live inside a project: parent title -> [titles]
CASES = {
    "Suspects": ["Main Menu Revamp"],
    "Tennis Clash – Social": ["Club Slam UX", "Clubs – Cheer Up"],
}
# Cover images (path inside the "Fernanda Nunes" export folder). Missing = placeholder.
COVERS = {
    "Suspects": "Work Projects/Suspects/Highlights/Main Menu Revamp/1.0_main_menu_revamp.png",
    "Main Menu Revamp": "Work Projects/Suspects/Highlights/Main Menu Revamp/1.0_main_menu_revamp.png",
    "Tennis Clash – Social": "Work Projects/Tennis Clash – Social/Club Slam UX/Untitled 6.png",
    "Club Slam UX": "Work Projects/Tennis Clash – Social/Club Slam UX/Untitled 6.png",
    "Clubs – Cheer Up": "Work Projects/Tennis Clash – Social/Clubs – Cheer Up/Untitled.png",
    "POS – Guerrilla": "Work Projects/POS – Guerrilla/Untitled.png",
    "Crush Hour: A GameJam Project": "Side Projects/Crush Hour A GameJam Project/wire06.png",
    "Fact Fuse": "Side Projects/Fact Fuse/FactFuse_Ipad_Game_MockUp_4.jpg",
    "Memo": "Side Projects/Memo/Untitled.png",
    "Política de Drogas é uma Questão de Mulheres": "Side Projects/Política de Drogas é uma Questão de Mulheres/Cartas_Back.jpg",
}
# "Result first" layout. top = sections that stay above the result (context);
# result = sections moved up; everything else goes under "The process".
LAYOUT = {
    "Club Slam UX": dict(top=[], result=["Live feature screens", "Know more"], lead_from="Intro"),
    "Main Menu Revamp": dict(top=[], result=["Final Result"], lead_from="Overview"),
}
PAGE_LANG = {"Política de Drogas é uma Questão de Mulheres": "pt-BR"}

# ----------------------------------------------------------------------------
# 2. HELPERS
# ----------------------------------------------------------------------------
def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "page"

def esc(s): return html.escape(s, quote=True)

def unq(s): return urllib.parse.unquote(s)

HASH_RE = re.compile(r" [0-9a-f]{32}(?=\.(md|csv)$)")
def strip_hash(name): return HASH_RE.sub("", name)

EXPORT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
DIST = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path("dist").resolve()
if EXPORT is None:
    sys.exit(__doc__)
ROOT = EXPORT / "Fernanda Nunes"
if not ROOT.exists():
    sys.exit(f"Could not find the folder 'Fernanda Nunes' inside {EXPORT}")

if DIST.exists(): shutil.rmtree(DIST)
for sub in ("assets/img", "assets/vid"): (DIST / sub).mkdir(parents=True, exist_ok=True)

IMG_CACHE = {}
def proc_image(path, maxw=2200, q=88):
    key = (str(path), maxw)
    if key in IMG_CACHE: return IMG_CACHE[key]
    digest = hashlib.sha1(path.read_bytes()).hexdigest()[:10]
    rel = f"assets/img/{digest}-{maxw}.webp"
    im = Image.open(path); im.load()
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA" if "A" in im.mode or im.mode == "P" else "RGB")
    if im.size[0] > maxw:
        im = im.resize((maxw, round(im.size[1] * maxw / im.size[0])), Image.LANCZOS)
    if not (DIST / rel).exists():
        im.save(DIST / rel, "WEBP", quality=q, method=4)
    IMG_CACHE[key] = dict(url=rel, w=im.size[0], h=im.size[1])
    return IMG_CACHE[key]

VID_CACHE = {}
def proc_video(path):
    if str(path) in VID_CACHE: return VID_CACHE[str(path)]
    digest = hashlib.sha1(path.read_bytes()).hexdigest()[:10]
    rel = f"assets/vid/{digest}.mp4"
    if not (DIST / rel).exists():
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(path),
                        "-vf", "scale='min(1280,iw)':-2:flags=lanczos,format=yuv420p",
                        "-c:v", "libx264", "-crf", "27", "-preset", "veryfast",
                        "-movflags", "+faststart", "-an", str(DIST / rel)], check=True)
    VID_CACHE[str(path)] = rel
    return rel

# ----------------------------------------------------------------------------
# 3. READ PAGES
# ----------------------------------------------------------------------------
class Page:
    def __init__(self, md_path, kind, parent=None):
        self.md_path = md_path
        self.dir = md_path.parent
        self.kind = kind            # work | side | case | about
        self.parent = parent
        text = md_path.read_text(encoding="utf-8").lstrip("\ufeff")
        lines = text.split("\n")
        self.title = lines[0][2:].strip() if lines[0].startswith("# ") else md_path.stem
        i, props = 1, {}
        while i < len(lines) and not lines[i].strip(): i += 1
        while i < len(lines) and lines[i].strip():
            m = re.match(r"^([^:]{1,30}): ?(.*)$", lines[i])
            if not m: break
            props[m.group(1).strip()] = m.group(2).strip(); i += 1
        self.props = props
        self.body = "\n".join(lines[i:]).strip()
        self.slug = slugify(self.title)
        self.children = []
        self.cover = COVERS.get(self.title)
        self.lang = PAGE_LANG.get(self.title, "en")
        self.size = "M"

    @property
    def roles(self): return self.props.get("My Role") or self.props.get("a") or ""
    @property
    def year(self):
        d = self.props.get("Date") or self.props.get("Created") or ""
        m = re.search(r"(19|20)\d\d", d); return m.group(0) if m else ""
    @property
    def occasion(self): return self.props.get("Occasion", "")
    @property
    def url(self):
        if self.kind == "case": return f"{self.parent.url}{self.slug}/"
        if self.kind == "about": return "about/"
        return f"{'work' if self.kind == 'work' else 'side'}/{self.slug}/"
    @property
    def depth(self): return self.url.count("/")

def find_md(directory, title):
    """Find the .md whose first line is '# title'."""
    for p in sorted(directory.glob("*.md")):
        first = p.read_text(encoding="utf-8").lstrip("\ufeff").split("\n", 1)[0]
        if first.strip() == f"# {title}": return p
    raise FileNotFoundError(f"No page titled '{title}' in {directory}")

PAGES, BY_BASENAME = [], {}
def register(page):
    PAGES.append(page); BY_BASENAME[page.md_path.name] = page

work_pages, side_pages = [], []
for title, size in WORK:
    pg = Page(find_md(ROOT / "Work Projects", title), "work"); pg.size = size
    register(pg); work_pages.append(pg)
    for ct in CASES.get(title, []):
        cdir = ROOT / "Work Projects" / pg.dir.name if False else None
        found = None
        for cand in (ROOT / "Work Projects").rglob("*.md"):
            if cand.read_text(encoding="utf-8").lstrip("\ufeff").split("\n", 1)[0].strip() == f"# {ct}":
                found = cand; break
        c = Page(found, "case", parent=pg); register(c); pg.children.append(c)
for title in SIDE:
    pg = Page(find_md(ROOT / "Side Projects", title), "side"); register(pg); side_pages.append(pg)
about = Page(find_md(ROOT, "About Me"), "about"); register(about)

# ----------------------------------------------------------------------------
# 4. MARKDOWN -> HTML
# ----------------------------------------------------------------------------
MD = MarkdownIt("commonmark", {"breaks": True, "html": True}).enable(["table", "strikethrough"])
ASIDE_GROUP = re.compile(r"(?:<aside>.*?</aside>[ \t]*\n?\s*)+", re.S)
ASIDE_ONE = re.compile(r"<aside>(.*?)</aside>", re.S)
EMOJI_START = re.compile(r"^([^\w\s<\[\(\*_#>`!-/:-@\\-`{-~]+)\s*")

def render_inline_md(s): return MD.render(s)

def build_aside(inner):
    inner = inner.strip()
    icon_html, rest = "", inner
    m = re.match(r'^<img [^>]*src="([^"]+)"[^>]*/?>\s*', inner)
    if m:
        icon_html = f'<img class="ic-img" src="{m.group(1)}" alt="">'
        rest = inner[m.end():]
    else:
        m = EMOJI_START.match(inner)
        if m: icon_html = f'<span class="ic" aria-hidden="true">{m.group(1)}</span>'; rest = inner[m.end():]
    link = re.fullmatch(r"[*_]*\[([^\]]+)\]\(([^)]+)\)[*_]*", rest.strip())
    if link:
        label = MD.renderInline(link.group(1))
        return ("link", f'<a class="linkcard" href="{link.group(2)}">{icon_html}<span>{label}</span></a>')
    body = render_inline_md(rest.strip())
    return ("call", f'<div class="callout">{icon_html}<div class="cbody">{body}</div></div>')

def md_to_html(text):
    groups = []
    def grp(m):
        items = [build_aside(a) for a in ASIDE_ONE.findall(m.group(0))]
        groups.append(items)
        return f"\n\n@@ASIDEGROUP{len(groups)-1}@@\n\n"
    text = ASIDE_GROUP.sub(grp, text)
    out = MD.render(text)
    def put(m):
        items = groups[int(m.group(1))]
        items = [it for it in items if "Back to top" not in it[1]]
        if not items: return ""
        if all(k == "link" for k, _ in items):
            return '<div class="linkrow">' + "".join(h for _, h in items) + "</div>"
        return '<div class="calloutrow">' + "".join(h for _, h in items) + "</div>"
    return re.sub(r"<p>@@ASIDEGROUP(\d+)@@</p>", put, out)

# ----------------------------------------------------------------------------
# 5. POST-PROCESS
# ----------------------------------------------------------------------------
GENERIC_ALT = re.compile(r"^(untitled.*|frame[ _]?\d+.*|image.*|.*\.(png|jpe?g|gif|webp))$", re.I)
YT_RE = re.compile(r"(?:youtube\.com/watch\?(?:[^#]*&)?v=|youtu\.be/)([\w-]{11})")

def norm(s): return re.sub(r"\W+", " ", s).strip().lower()

def tag(soup, name, cls=None, **attrs):
    t = soup.new_tag(name, **{k.replace("_", "-"): v for k, v in attrs.items()})
    if cls: t["class"] = cls
    return t

def wix_original(url):
    m = re.match(r"(https://static\.wixstatic\.com/media/[^/]+)/v1/.*", url)
    return m.group(1) if m else url

def media_for(img_src, page_dir, soup, alt="", icon=False):
    """Return (kind, element) for an image/gif/mp4 reference."""
    if img_src.startswith("http"):
        el = tag(soup, "img", src=img_src, alt=alt, loading="lazy", referrerpolicy="no-referrer")
        el["data-full"] = wix_original(img_src); el["data-remote"] = "1"
        return "img", el
    path = page_dir / unq(img_src)
    if not path.exists():
        print("  ! missing file:", path.name); return None, None
    ext = path.suffix.lower()
    if ext in (".gif", ".mp4", ".mov", ".webm"):
        rel = proc_video(path)
        v = tag(soup, "video", src="@@ROOT@@" + rel, muted="", playsinline="", preload="metadata")
        if ext == ".gif": v["autoplay"] = ""; v["loop"] = ""
        else: v["controls"] = ""
        return "video", v
    info = proc_image(path, 160 if icon else 2200)
    el = tag(soup, "img", src="@@ROOT@@" + info["url"], alt=alt, width=info["w"], height=info["h"], loading="lazy")
    if not icon: el["data-full"] = "@@ROOT@@" + info["url"]
    return "img", el

def process_html(page, raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    d = page.dir

    # 5a. heading levels: compact to h2..h5, add ids
    lv = sorted({int(h.name[1]) for h in soup.find_all(re.compile(r"^h[1-6]$"))})
    mapping = {l: min(2 + i, 5) for i, l in enumerate(lv)}
    used = set()
    for h in soup.find_all(re.compile(r"^h[1-6]$")):
        h.name = f"h{mapping[int(h.name[1])]}"
        strs = list(h.strings)
        if strs and strs[0].lstrip().startswith("::"): strs[0].replace_with(strs[0].lstrip().lstrip(":").lstrip())
        strs = list(h.strings)
        if strs and strs[-1].rstrip().endswith(":"): strs[-1].replace_with(strs[-1].rstrip().rstrip(":").rstrip())
        text = h.get_text(" ", strip=True)
        base = slugify(text) or "section"; sid, n = base, 2
        while sid in used: sid = f"{base}-{n}"; n += 1
        used.add(sid); h["id"] = sid

    # 5b. icons inside link cards / callouts
    for img in soup.select("img.ic-img"):
        kind, el = media_for(img["src"], d, soup, icon=True)
        if el is None: img.replace_with(NavigableString("▶")); continue
        el["class"] = ["ic-img"]; el["alt"] = ""; img.replace_with(el)

    # 5c. paragraphs that are only an image / video / youtube link -> figures
    top = [c for c in soup.contents if not (isinstance(c, NavigableString) and not c.strip())]
    for p in [c for c in top if getattr(c, "name", None) == "p"]:
        kids = [c for c in p.contents if not (isinstance(c, NavigableString) and not c.strip())]
        if len(kids) != 1: continue
        k = kids[0]
        if k.name == "img":
            alt = k.get("alt", "").strip()
            kind, el = media_for(unq(k["src"]) if not k["src"].startswith("http") else k["src"], d, soup,
                                 alt="" if GENERIC_ALT.match(alt) else alt)
            if el is None: p.decompose(); continue
            fig = tag(soup, "figure", ["wide", "fig"]); fig.append(el)
            if kind == "img" and alt and not GENERIC_ALT.match(alt):
                cap = tag(soup, "figcaption"); cap.string = alt.strip("*_ "); fig.append(cap)
            p.replace_with(fig)
        elif k.name == "a":
            href = k.get("href", "")
            ym = YT_RE.search(href)
            if ym:
                wrap = tag(soup, "div", ["wide", "embed"])
                fr = tag(soup, "iframe", src=f"https://www.youtube-nocookie.com/embed/{ym.group(1)}",
                         title="Video", loading="lazy", allowfullscreen="")
                fr["allow"] = "accelerometer; encrypted-media; picture-in-picture"
                wrap.append(fr); p.replace_with(wrap)
            elif unq(href).lower().endswith(".mp4"):
                kind, el = media_for(href, d, soup)
                if el is not None:
                    fig = tag(soup, "figure", ["wide", "fig"]); fig.append(el); p.replace_with(fig)

    # 5d. captions: drop the italic duplicate of an alt caption; adopt short italic caption otherwise
    for fig in soup.select("figure.fig"):
        nxt = fig.find_next_sibling()
        while nxt is not None and isinstance(nxt, NavigableString): nxt = nxt.next_sibling
        if nxt is None or nxt.name != "p": continue
        kids = [c for c in nxt.contents if not (isinstance(c, NavigableString) and not c.strip())]
        if len(kids) == 1 and kids[0].name == "em":
            ctext = kids[0].get_text(" ", strip=True)
            existing = fig.find("figcaption")
            if existing and norm(existing.get_text()) == norm(ctext): nxt.decompose()
            elif not existing and len(ctext) < 220:
                cap = tag(soup, "figcaption"); cap.string = ctext; fig.append(cap); nxt.decompose()

    # 5e. galleries: runs of figures
    top = [c for c in soup.contents if not (isinstance(c, NavigableString) and not c.strip())]
    run = []
    def flush():
        nonlocal run
        if len(run) >= 2 and all(f.find("img") for f in run):
            remote = all(f.find("img").has_attr("data-remote") for f in run)
            portrait = all(f.find("img").get("width") and int(f.find("img")["height"]) >= int(f.find("img")["width"]) * 0.9 for f in run)
            if remote or portrait:
                g = tag(soup, "div", ["wide", "gallery"])
                cols = min(len(run), 4) if portrait else (3 if len(run) % 3 == 0 else 2)
                g["style"] = f"--cols:{cols}"
                run[0].insert_before(g)
                for f in run:
                    f["class"] = ["fig"]; g.append(f.extract())
        run = []
    for n in top:
        if getattr(n, "name", None) == "figure" and "fig" in (n.get("class") or []): run.append(n)
        else: flush()
    flush()

    # 5f. tables, notes
    for t in soup.find_all("table"):
        w = tag(soup, "div", ["wide", "tablewrap"]); t.insert_before(w); w.append(t.extract())
    for p in soup.find_all("p"):
        if p.get_text(strip=True) == "[more soon]":
            p["class"] = ["note"]; p.string = "More details coming soon."

    # 5g. links
    heading_ids = {norm(h.get_text(" ", strip=True)): h["id"] for h in soup.find_all(re.compile(r"^h[2-5]$"))}
    case_cards = []
    for a in list(soup.find_all("a")):
        href = a.get("href", "")
        if not href or href.startswith(("#", "mailto:")): continue
        if href.startswith("http"):
            a["target"] = "_blank"; a["rel"] = "noopener"; continue
        base = unq(href).split("/")[-1].split("#")[0]
        if base.endswith(".csv"):
            host = a.find_parent("p") or a
            slot = tag(soup, "div", ["slot"]); slot["data-slot"] = "cases" if "Highlights" in base else "favorites"
            host.replace_with(slot); continue
        target = BY_BASENAME.get(base)
        if target is page:
            label = norm(a.get_text())
            a["href"] = "#" + heading_ids.get(label, heading_ids.get("detailed process", "process"))
            del a["target"]
        elif target is not None:
            only_link = a.parent is soup and False
            par = a.find_parent("p")
            if par is not None and par.parent is soup and len(par.get_text(strip=True)) == len(a.get_text(strip=True)) and target.kind == "case":
                case_cards.append(target)
                if len([x for x in soup.select('div.slot[data-slot="cases"]')]) == 0:
                    slot = tag(soup, "div", ["slot"]); slot["data-slot"] = "cases"; par.replace_with(slot)
                else: par.decompose()
            else:
                a["href"] = "@@ROOT@@" + target.url
        else:
            print(f"  ! unresolved link in '{page.title}': {href[:60]}")
    return soup

# ----------------------------------------------------------------------------
# 6. ARTICLE ASSEMBLY (lead, result-first layout, toc)
# ----------------------------------------------------------------------------
def heading_level(n): return int(n.name[1]) if getattr(n, "name", None) and re.fullmatch(r"h[2-5]", n.name) else None

def extract_section(nodes, title):
    t = norm(title)
    for i, n in enumerate(nodes):
        lvl = heading_level(n)
        if lvl and norm(n.get_text(" ", strip=True)).startswith(t):
            j = i + 1
            while j < len(nodes) and not (heading_level(nodes[j]) and heading_level(nodes[j]) <= lvl): j += 1
            sec = nodes[i:j]; del nodes[i:j]
            return sec
    return []

def render_nodes(nodes): return "".join(str(n) for n in nodes)

def assemble(page, soup):
    nodes = [c for c in soup.contents if not (isinstance(c, NavigableString) and not c.strip())]
    # lead = first italic paragraph / blockquote near the top
    lead = ""
    for n in nodes[:6]:
        if n.name == "blockquote" or (n.name == "p" and len([c for c in n.contents if not (isinstance(c, NavigableString) and not c.strip())]) == 1 and n.find("em")):
            inner = n.find("p") if n.name == "blockquote" else n
            lead = inner.decode_contents(); nodes.remove(n); break
    cfg = LAYOUT.get(page.title)
    if not lead and cfg and cfg.get("lead_from"):
        t = norm(cfg["lead_from"])
        for i, n in enumerate(nodes):
            if heading_level(n) and norm(n.get_text(" ", strip=True)).startswith(t):
                for m in nodes[i + 1:]:
                    if m.name == "p": lead = m.decode_contents(); nodes.remove(m); break
                    if heading_level(m): break
                break
    # drop a divider right after the lead
    if nodes and nodes[0].name == "hr": nodes.pop(0)
    toc_nodes = nodes
    html_parts, has_result = [], False
    if cfg:
        has_result = True
        top = [x for t in cfg["top"] for x in extract_section(nodes, t)]
        result = []
        for t in cfg["result"]:
            sec = extract_section(nodes, t)
            if sec and heading_level(sec[0]): sec[0].name = "h2"
            result += sec
        # remaining content is the process
        html_parts.append(render_nodes(top))
        html_parts.append('<section class="block" id="result">' + render_nodes(result) + "</section>")
        html_parts.append('<h2 id="process" class="process-title">The process</h2>')
        html_parts.append(render_nodes(nodes))
    else:
        html_parts.append(render_nodes(nodes))
    body = "".join(html_parts)
    return lead, body, has_result

def make_toc(body):
    s = BeautifulSoup(body, "html.parser")
    hs = [h for h in s.find_all(["h2", "h3"]) if h.get("id")]
    if len([h for h in hs if h.name == "h2"]) < 3 and len(hs) < 5: return ""
    if len(hs) > 16: hs = [h for h in hs if h.name == "h2"]
    items = "".join(f'<li class="{h.name}"><a href="#{h["id"]}">{esc(h.get_text(" ", strip=True).rstrip(":"))}</a></li>' for h in hs)
    return f'<nav class="toc" aria-label="On this page"><ol>{items}</ol></nav>'

# ----------------------------------------------------------------------------
# 7. TEMPLATES
# ----------------------------------------------------------------------------
def thumb(page, width=900):
    if page.cover and (ROOT / page.cover).exists():
        info = proc_image(ROOT / page.cover, width, 84)
        return f'<div class="thumb"><img src="@@ROOT@@{info["url"]}" width="{info["w"]}" height="{info["h"]}" alt="" loading="lazy"></div>'
    hue = int(hashlib.sha1(page.title.encode()).hexdigest()[:4], 16) % 60 + 235
    words=[w for w in re.findall(r"[A-Za-zÀ-ÿ0-9#]+", page.title) if w.lower() not in ("a","of","the","de","da","do","é","uma","and")]
    ini="".join(w[0].upper() for w in words[:2])
    return f'<div class="thumb ph" style="--h:{hue}" aria-hidden="true"><span>{esc(ini)}</span></div>'

def card(page, size="M", side=False):
    sub = esc(page.roles)
    if side:
        extra = ", ".join(x for x in (page.occasion, page.year) if x)
        sub = f'{esc(page.roles)}<br><span class="dim">{esc(extra)}</span>'
    return (f'<a class="card s{size}" href="@@ROOT@@{page.url}">{thumb(page)}'
            f'<div class="ctext"><h3>{esc(page.title)}</h3><p>{sub}</p></div></a>')

HEAD_FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
              '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
              '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800'
              '&family=Hanken+Grotesk:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%231B1740'/%3E%3Cpath d='M32 10l5.5 16.5L54 32l-16.5 5.5L32 54l-5.5-16.5L10 32l16.5-5.5z' fill='%23A78BFA'/%3E%3C/svg%3E")

def shell(title, desc, body, depth, active="", lang="en"):
    root = "../" * depth if depth else "./"
    def nav(label, href, key): 
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    email_noscript = f'{SITE["email_user"]} [at] {SITE["email_domain"]}'
    page = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta name="theme-color" content="#1B1740">
<link rel="icon" href="{FAVICON}">
{HEAD_FONTS}
<link rel="stylesheet" href="@@ROOT@@assets/style.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="brand" href="@@ROOT@@">{esc(SITE["name"])}</a>
  <nav class="primary" aria-label="Main">
    {nav("Work", "@@ROOT@@#work", "work")}
    {nav("Side projects", "@@ROOT@@#side", "side")}
    {nav("About", "@@ROOT@@about/", "about")}
    <a href="#contact">Contact</a>
  </nav>
  <div class="actions">
    <a href="{SITE["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a>
    <a href="{SITE["resume"]}" target="_blank" rel="noopener">Resume</a>
    <button type="button" id="theme" aria-label="Switch light and dark theme"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M21 13.5A9 9 0 1 1 10.5 3a7 7 0 0 0 10.5 10.5z" fill="currentColor"/></svg></button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site" id="contact">
  <h2>Let’s talk</h2>
  <p>Contact me on LinkedIn or send an email.</p>
  <p class="links">
    <a class="btn" href="{SITE["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a>
    <a class="btn ghost mail" href="#" data-u="{SITE["email_user"]}" data-d="{SITE["email_domain"]}">{email_noscript}</a>
    <a class="btn ghost" href="{SITE["resume"]}" target="_blank" rel="noopener">Resume</a>
  </p>
  <small>© {SITE["year"]} {esc(SITE["name"])}</small>
</footer>
<button type="button" id="top" aria-label="Back to top">↑</button>
<script src="@@ROOT@@assets/site.js" defer></script>
</body>
</html>'''
    return page.replace("@@ROOT@@", root)

def meta_dl(page):
    rows = []
    if page.roles: rows.append(("Role" if page.kind != "case" else "Focus", page.roles))
    if page.occasion: rows.append(("Occasion", page.occasion))
    if page.year: rows.append(("Year", page.year))
    if not rows: return ""
    return '<dl class="meta">' + "".join(f"<div><dt>{k}</dt><dd>{esc(v)}</dd></div>" for k, v in rows) + "</dl>"

def related(page):
    group = work_pages if (page.kind == "work" or (page.kind == "case" and page.parent.kind == "work")) else side_pages
    base = page.parent if page.kind == "case" else page
    i = group.index(base)
    picks = [group[(i + k) % len(group)] for k in (1, 2, 3)]
    return picks

def article_page(page):
    raw = md_to_html(page.body)
    soup = process_html(page, raw)
    lead, body, has_result = assemble(page, soup)

    # fill slots
    sb = BeautifulSoup(body, "html.parser")
    for slot in sb.select("div.slot"):
        if slot["data-slot"] == "cases":
            cards = "".join(card(c) for c in page.children)
            slot.replace_with(BeautifulSoup(f'<section class="wide cases"><h2>Case studies</h2><div class="grid cases-grid">{cards}</div></section>', "html.parser"))
        else:
            slot.decompose()
    body = str(sb)
    toc = make_toc(body)

    back = ""
    if page.kind == "case": back = f'<a class="back" href="@@ROOT@@{page.parent.url}">← {esc(page.parent.title)}</a>'
    elif page.kind in ("work", "side"):
        back = f'<a class="back" href="@@ROOT@@#{"work" if page.kind=="work" else "side"}">← {"Work" if page.kind=="work" else "Side projects"}</a>'
    cta = '<p class="cta"><a class="btn" href="#process">Read the full process</a></p>' if has_result else ""
    header = (f'<header class="phead">{back}<h1>{esc(page.title)}</h1>'
              + (f'<p class="lead">{lead}</p>' if lead else "") + meta_dl(page) + cta + "</header>")
    rel_cards = ""
    if page.kind != "about":
        rel_cards = ('<section class="related wide"><h2>More projects</h2><div class="grid rel">'
                     + "".join(card(r) for r in related(page)) + "</div></section>")
    inner = f'<div class="article">{header}{body}</div>'
    main = f'{toc}{inner}{rel_cards}'
    desc = re.sub(r"<[^>]+>", "", lead)[:200] or f"{page.title}, a project by {SITE['name']}."
    return shell(f"{page.title} | {SITE['name']}", desc, main, page.depth, active=("work" if page.kind in ("work", "case") and page.parent is None or (page.kind=="case" and page.parent.kind=="work") else page.kind), lang=page.lang)

def about_page(page):
    raw = md_to_html(page.body)
    soup = process_html(page, raw)
    lead, body, _ = assemble(page, soup)
    fav_dir = page.dir / "About Me" / "Even more about me"
    # favorites come from the CSV + subpages
    favs = []
    csv_files = [p for p in (page.dir / "About Me").glob("Even more about me*.csv") if not p.name.endswith("_all.csv")]
    import csv
    for row in csv.DictReader(csv_files[0].open(encoding="utf-8-sig")):
        name = row["Name"]
        img = next((p for p in (page.dir / "About Me" / "Even more about me" / name).glob("*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")), None) if (page.dir / "About Me" / "Even more about me" / name).exists() else None
        if img: favs.append((name, row["Tags"], proc_image(img, 700, 84)))
    cards = "".join(f'<figure class="fav"><img src="@@ROOT@@{i["url"]}" width="{i["w"]}" height="{i["h"]}" alt="{esc(n)}" loading="lazy"><figcaption><strong>{esc(n)}</strong><span>{esc(t)}</span></figcaption></figure>' for n, t, i in favs)
    sb = BeautifulSoup(body, "html.parser")
    if not lead:
        h = sb.find(re.compile(r"^h[2-5]$"))
        if h: lead = esc(h.get_text(" ", strip=True)); h.decompose()
    for slot in sb.select("div.slot"):
        slot.replace_with(BeautifulSoup(f'<section class="wide favs"><h2>Even more about me</h2><div class="favgrid">{cards}</div></section>', "html.parser"))
    body = str(sb)
    header = (f'<header class="phead"><h1>About me</h1><p class="lead">{lead}</p>'
              f'<p class="cta"><a class="btn" href="{SITE["resume"]}" target="_blank" rel="noopener">Resume</a> '
              f'<a class="btn ghost" href="{SITE["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a></p></header>')
    return shell(f"About | {SITE['name']}", "About Fernanda Nunes, interdisciplinary designer.", f'<div class="article">{header}{body}</div>', 1, active="about")

def home_page():
    work = "".join(card(p, p.size) for p in work_pages)
    side = "".join(card(p, "S", side=True) for p in side_pages)
    body = f'''<section class="intro">
  <h1>{esc(SITE["name"])}</h1>
  <p class="lead">{SITE["intro_html"]}</p>
</section>
<section id="work" class="band"><h2>Work</h2><div class="grid work-grid">{work}</div></section>
<section id="side" class="band"><h2>Side projects</h2><div class="grid side-grid">{side}</div></section>'''
    return shell(f"{SITE['name']} | Senior Game UX Designer", "Portfolio of Fernanda Nunes, interdisciplinary designer and Senior Game UX Designer.", body, 0)

def write(rel, content):
    p = DIST / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content, encoding="utf-8")

# ----------------------------------------------------------------------------
# 8. BUILD
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    here = Path(__file__).parent
    shutil.copy(here / "style.css", DIST / "assets" / "style.css")
    shutil.copy(here / "site.js", DIST / "assets" / "site.js")
    write("index.html", home_page())
    for pg in PAGES:
        print("building", pg.url)
        write(pg.url + "index.html", about_page(pg) if pg.kind == "about" else article_page(pg))
    write("404.html", shell("Page not found | " + SITE["name"], "Page not found",
          '<div class="article"><header class="phead"><h1>Page not found</h1><p class="lead">This page does not exist. Try the <a href="/">home page</a>.</p></header></div>', 0))
    (DIST / ".nojekyll").write_text("")
    total = sum(f.stat().st_size for f in DIST.rglob("*") if f.is_file())
    print(f"done: {total/1e6:.1f} MB in {DIST}")
