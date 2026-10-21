# Fernanda Nunes | Portfolio

A simple static site for GitHub Pages. No build step: edit the files, upload them, done.

## Files

- `index.html` is the site itself. You should not need to touch it.
- `content.js` is the home page: intro, experience, the list of projects, contact.
- `projects/` has one text file per project. `about.md` is the About page.
- `images/` has every picture and animation.
- `icon.svg`, `favicon-32.png`, `favicon.ico` and `apple-touch-icon.png` are the site icon (black and white).

## Adding or replacing an image

Every gray box on the site shows a file name in its corner (for example `abf-design-01`).
Put a file with that name in `images/` and the box turns into the image. Nothing else to edit.

- Formats: `.jpg`, `.png`, `.webp`, `.gif` or `.mp4`. An `.mp4` or `.gif` wins over a still image with the same name.
- Project thumbnails on the home page use the project name, for example `images/suspects.jpg`.
- Images are shown at most as wide as the text column, never stretched past their own size. Clicking an image opens it larger (click again for 100%, Esc to close).
- Exported at 2x? Add `@2x` to the name (`name@2x.png`, and the same in the text file) and it shows at half size.
- Replacing an image: upload a file with the same name. If the old one has a different extension, delete it.

## Writing and editing

Project pages are plain text, written like Notion:

- `## Heading`, `### Smaller heading`, `- bullet`, `1. numbered`, `**bold**`, `*italic*`, `[link text](https://...)`
- An image: `![Caption](image-name|16:9)`. The ratio (16:9, 4:3, 3:4...) sets the gray box before the image exists.
- Several image lines in a row (no blank line between them) sit side by side in boxes of the same size.
- Sections that open on click (like the steps in Angry Birds Friends):

      :::tracks
      Step name | One line about it
      Another step | One line about it
      :::

      :::track Step name
      Text and images of this step.
      :::

  The names after `:::track` must match the names in the list.

## Show, hide or reorder projects

In `content.js`: the list under "Selected Works" and "Side Projects" decides what shows and in which order.
A project that is commented out in `projects: { ... }` is hidden (Angry Birds Dream Blast is hidden now).

## Preview on your computer

1. Install VS Code and the "Live Server" extension.
2. Open this folder, right click `index.html`, choose "Open with Live Server".
3. Every time you save a file, the page updates.

Opening `index.html` by double-clicking will not load the text files, because browsers block that. Use Live Server.

## Publishing

Upload the files to the repository (Add file > Upload files, or GitHub Desktop: Commit and Push). The site updates in a minute or two.
