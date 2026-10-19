# Fernanda Nunes | Portfolio

Site estatico (HTML, CSS e JS puros) para o GitHub Pages. Nao precisa de build para publicar.

## Onde ficam as imagens
Cada projeto tem a sua pasta dentro de `assets/`, com nomes legiveis:

- `assets/suspects/cover.webp` = capa do Suspects (a que aparece na home)
- `assets/suspects/main-menu-revamp/` = imagens do case Main Menu Revamp
- `assets/tennis-clash-social/club-slam-ux/` = imagens do case Club Slam
- `assets/about/` = jogos favoritos da pagina About

**Para trocar uma imagem:** salve a nova no formato `.webp` (ou `.png`/`.jpg`, mas ai o nome do arquivo muda e e preciso ajustar o HTML), com o MESMO nome e na MESMA pasta, e envie por cima da antiga.
**Para trocar uma capa:** substitua o `cover.webp` da pasta do projeto. Qualquer proporcao funciona, ela e recortada automaticamente.

## Ver o site no computador antes de publicar
1. Instale o VS Code (code.visualstudio.com) e a extensao **Live Server**.
2. Abra a pasta do site no VS Code, clique com o botao direito em `index.html` e escolha **Open with Live Server**.
3. O site abre em `http://127.0.0.1:5500` e atualiza sozinho cada vez que voce salva um arquivo.
Alternativa sem instalar nada: no Terminal, dentro da pasta do site, rode `python3 -m http.server 8000` e abra `http://localhost:8000`.

## Publicar
Quando estiver satisfeita, envie os arquivos alterados para o repositorio (GitHub Desktop: Commit e Push; ou pelo site: Add file > Upload files > Commit changes).

## Editar
- **Cores, fontes e espacamentos:** `assets/style.css` (as cores ficam no inicio, em `:root`).
- **Textos pequenos:** edite direto o `.html` da pagina.
- **Atencao:** a pasta `_builder` gera o site inteiro a partir do export do Notion. Se rodar o build de novo, ele sobrescreve edicoes feitas a mao nos `.html`. Escolha um jeito e mantenha: editar a mao, ou editar pelo builder.
