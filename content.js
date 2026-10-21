/* =====================================================================
   CONTENT OF THE SITE
   This is the only file you need to edit to change the home page.
   Project pages are plain text files in the "projects" folder
   (projects/suspects.md, ...) and the About page is "about.md".
   Images go in the "images" folder (see README.md).
   Be careful to keep every comma, quote and bracket in place.
   ===================================================================== */
window.SITE = {
  name: "Fernanda Nunes",

  /* ---------- Every project that has its own page ----------
     key       = file name in "projects" (suspects -> projects/suspects.md)
     title     = name shown on the home page and at the top of the page
     line      = one-line description
     meta      = small lines under the title: [ "UX Designer, Researcher", "Global Game Jam, 2021" ]
     pageLine  = (optional) a different subtitle for the project page; "" hides it
     thumb     = (optional) image name for the small picture; default is the key
                 (suspects -> images/suspects.jpg)                                  */
  projects: {
    "angry-birds-friends":   { title: "Angry Birds Friends",   line: "Improving usability in Level Design",
                               meta: ["UX Designer, Researcher, Creative Designer"] },
    /* HIDDEN FOR NOW: to show it again, remove these comment marks and add "angry-birds-dream-blast" back to the Selected Works list below
    "angry-birds-dream-blast": { title: "Angry Birds Dream Blast", line: "Revamping events’ framework" },
    */
    "afk-football":          { title: "AFK Football",          line: "Adapting AFK rewards to football theme",
                               meta: ["UX Designer"] },
    "corpcity":              { title: "Corpcity",              line: "Redesigning the city’s managers",
                               meta: ["UX Designer"] },
    "suspects":              { title: "Suspects",              line: "Revamping the Main Menu",
                               meta: ["UX Designer"] },
    "tennis-clash":          { title: "Tennis Clash",          line: "Creating a weekly team competition",
                               meta: ["UX Designer"] },

    "crush-hour":            { title: "Crush Hour",            line: "Global Game Jam", pageLine: "",
                               meta: ["Game Design, Product Management, UX/UI", "Global Game Jam, 2021"] },
    "coup":                  { title: "Coup",                  line: "Dinosaurs & 2nd WW Ed.",
                               meta: ["Visual Designer", "Personal project, 2019"] },
    "alien-cable":           { title: "Alien Cable",           line: "Global Game Jam", pageLine: "",
                               meta: ["Game Design, UX/UI", "Global Game Jam, 2018"] },
    "nasty-island":          { title: "Nasty Island",          line: "Global Game Jam", pageLine: "",
                               meta: ["Game Design, Product Management, Visual Designer", "Global Game Jam, 2017"] }
  },

  /* ---------- About page (text is in about.md) ---------- */
  about: { title: "About me", line: "" },

  /* ---------- Home page: a list of sections, shown from top to bottom ----------
     To ADD a section: copy one block below, paste it where you want it, and edit.
     To REMOVE or MOVE one: delete or cut and paste the whole block { ... },
     Section types:
       intro     big title + text + optional link to a page
       timeline  dates and roles                  items: [ ["date", "Role @ Company", "company link (optional)"], ... ]
       list      projects with a picture on the left   items: [ "project-key", ... ]
       grid      projects in two columns               items: [ "project-key", ... ]
       links     links with a small icon (images/icon-email.png, images/icon-linkedin.png)
       text      a free text section (you can use **bold**, *italic*, [links](https://...))   */
  home: [
    { type: "intro",
      title: "Hey, I’m Fernanda!",
      text: `I’m an interdisciplinary designer with 12 years of experience across research, product, and design, with the last five focused on mobile games.

I specialize in game systems and player experiences: figuring out why players do what they do and translating that into seamless, distinctive gameplay. I’m a big fan of solving hard problems and making small experimental games, and I’ve been active in the game jam scene since 2011.`,
      more: { text: "Do you want to know more?", to: "about" } },

    { type: "timeline",
      title: "Experience",
      items: [
        ["May 2023 – Present", "Senior UX & Creative Designer @ Rovio", "https://www.rovio.com"],
        ["May 2022 – May 2023", "Senior UX Designer @ Wildlife", "https://wildlifestudios.com"],
        ["Jan 2022 – May 2022", "Senior Product Designer @ Nubank", "https://nubank.com.br"],
        ["Aug 2020 – Dec 2021", "UX Designer @ Wildlife", "https://wildlifestudios.com"],
        ["Dec 2018 – Aug 2020", "UX Designer @ PagBank", "https://pagbank.com.br"]
      ] },

    { type: "list",
      title: "Selected Works",
      items: ["angry-birds-friends", "suspects", "tennis-clash", "afk-football", "corpcity"] },

    { type: "grid",
      title: "Side Projects",
      items: ["crush-hour", "coup", "alien-cable", "nasty-island"] },

    { type: "links",
      title: "Let’s Talk",
      items: [
        { text: "fernandauxd@gmail.com", url: "mailto:fernandauxd@gmail.com", icon: "icon-email" },
        { text: "LinkedIn", url: "https://www.linkedin.com/in/nandanunes/", icon: "icon-linkedin" }
      ] }
  ]
};
