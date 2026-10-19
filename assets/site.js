(function () {
  var doc = document.documentElement;

  // Theme toggle (remembers the choice)
  var themeBtn = document.getElementById("theme");
  if (themeBtn) themeBtn.addEventListener("click", function () {
    var dark = doc.dataset.theme ? doc.dataset.theme === "dark"
      : window.matchMedia("(prefers-color-scheme: dark)").matches;
    var next = dark ? "light" : "dark";
    doc.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (e) {}
  });

  // Back to top
  var top = document.getElementById("top");
  if (top) {
    window.addEventListener("scroll", function () { top.classList.toggle("show", window.scrollY > 600); }, { passive: true });
    top.addEventListener("click", function () { window.scrollTo({ top: 0 }); });
  }

  // Email address assembled in the browser (keeps it out of simple scrapers)
  document.querySelectorAll("a.mail").forEach(function (a) {
    var addr = a.dataset.u + "@" + a.dataset.d;
    a.href = "mailto:" + addr; a.textContent = addr;
  });

  // Image lightbox: click to open, click again to toggle 100% size, Esc to close
  var lb;
  function closeLb() { if (lb) { lb.remove(); lb = null; document.body.style.overflow = ""; } }
  document.addEventListener("click", function (e) {
    var img = e.target.closest && e.target.closest("figure.fig img");
    if (!img) return;
    var fig = img.closest("figure"), cap = fig.querySelector("figcaption");
    lb = document.createElement("div"); lb.className = "lb"; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-modal", "true");
    var big = document.createElement("img"); big.src = img.dataset.full || img.src; big.alt = img.alt || "";
    var close = document.createElement("button"); close.type = "button"; close.textContent = "Close";
    lb.appendChild(big); lb.appendChild(close);
    if (cap) { var c = document.createElement("div"); c.className = "cap"; c.textContent = cap.textContent; lb.appendChild(c); }
    big.addEventListener("click", function (ev) { ev.stopPropagation(); lb.classList.toggle("full"); });
    lb.addEventListener("click", closeLb); close.addEventListener("click", closeLb);
    document.body.appendChild(lb); document.body.style.overflow = "hidden"; close.focus();
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeLb(); });

  // Highlight the current section in the table of contents
  var links = document.querySelectorAll(".toc a");
  if (links.length && "IntersectionObserver" in window) {
    var map = {};
    links.forEach(function (a) { var t = document.getElementById(a.getAttribute("href").slice(1)); if (t) map[t.id] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { links.forEach(function (l) { l.classList.remove("on"); }); map[en.target.id].classList.add("on"); }
      });
    }, { rootMargin: "-15% 0px -75% 0px" });
    Object.keys(map).forEach(function (id) { io.observe(document.getElementById(id)); });
  }
})();
