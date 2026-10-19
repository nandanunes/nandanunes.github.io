# Fernanda Nunes | Portfolio

Site estatico (HTML, CSS e JS puros), pronto para o GitHub Pages. Nao precisa de build para publicar.

## Como publicar
1. Crie um repositorio publico chamado `SEU-USUARIO.github.io`.
2. Envie TODO o conteudo desta pasta para a raiz do repositorio (Add file > Upload files). O `index.html` precisa ficar na raiz, e o arquivo `.nojekyll` tambem.
3. Settings > Pages > Deploy from a branch > `main` / `(root)` > Save.
4. Em 1 ou 2 minutos o site abre em `https://SEU-USUARIO.github.io`.

## Como editar
- **Cores, fontes e espacamentos:** `assets/style.css` (as cores ficam nas primeiras linhas, em `:root`).
- **Textos e ordem dos projetos:** `_builder/build.py` (listas `WORK`, `SIDE`, `COVERS`, `LAYOUT` no topo) e depois rodar o build.
- **Rodar o build** (precisa de Python 3 com `markdown-it-py`, `beautifulsoup4` e `Pillow`, e do `ffmpeg`):
  `python3 _builder/build.py "caminho/do/export-do-notion" dist`
  O site novo sai na pasta `dist`. Substitua os arquivos do repositorio por ele.

## O que ainda falta
- **Capas:** o Notion nao exporta as capas dos projetos. Os projetos sem imagem aparecem com um bloco colorido e iniciais (Angry Birds Friends, AFK Football, Corpcity, Customer Segmentation e a maioria dos side projects). Para trocar, informe o caminho da imagem em `COVERS` no `build.py`.
- **Imagens do Wix:** 62 imagens de side projects ainda estao hospedadas no Wix (links externos). Se voce fechar o Wix, elas somem. O ideal e baixar e colocar na pasta do export antes de rodar o build de novo.
