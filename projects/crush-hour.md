***Crush Hour** is a game about helping people who are looking for their subway crush. Working at a Crush Booth™ your job is to make a facial composite based on the description that is given to you. But dealing with vague descriptions, a crappy computer and a very slow printer are not your only challenges, because besides that your customers have little to no patience and everything gets even crazier during rush hour. On the bright side, at least you are helping people find love! Or you might as well be creating a bunch of stalkers... Luckily, worrying about that is not in your job description!*

![The final version of the game.](crush-hour-21)

## Overview

**Crush Hour** is a fast-paced, time and resource-managing game developed using Unity. It was made for the Global Game Jam 2021 (remote edition), and the theme was **Lost and Found**. You can [download the game for Windows](https://globalgamejam.org/2021/games/crush-hour-4).

Here I detail the process we used to create the game, from the brainstorming sessions to the game design and gameplay rhythm. Due to the remote aspect of the event, the Global Game Jam started on a Wednesday, but we started the development on Friday night as usual, since most of the team had full-time jobs.

### How we made it

Select a phase to read more about it:

:::tracks
Discovery | Brainstorming and selecting promising ideas for our game
Define | Converging our findings into a strong game idea
Planning | Defining our loop to execute our idea in two days
Production | Art, narrative, UX/UI, code, sound and logo
:::

:::track Discovery
After the reveal of the theme, we gathered together in Discord and started brainstorming. Time was limited since not everyone could dedicate themselves fully to the event. Our goal was to have a clear core mechanic for our game by Friday, so the developers could start coding as soon as possible.

### Brainstorming

*Method: listing ideas and voting. Session time: 1 hour.*

Our first Brainstorming Session goal was to generate as many ideas as possible using the theme **Lost and Found** as the core. To help the process, we created a central question: **What comes to your mind when you think about Lost and Found?**

For 5 minutes, we wrote down everything that came to our minds using the tool Miro. After writing everything down, we grouped the ideas by similarity and then voted for the ones we liked the most.

![](crush-hour-01|16:9)

Then we separated the three most voted groups of ideas and started another voting session, now focusing on the most promising concept from each one.

![](crush-hour-02|16:9)

As a result, we ended up with three possible paths to start building our game:

1. Objects that go missing because they go to other dimensions
2. The Finder: a person who finds lost objects for people
3. The Lost and Found and the weird objects that exist there

![](crush-hour-03|16:9)

### Napkin Pitch

The Napkin Pitch is a simple and easy method to convey a new idea, covering the most critical components associated with it. For our game, the main components we used were:

1. **Idea’s description.** Describe in a few words: What is the main goal of the game? Is the game a combination of the other two games? Example: “Pokemon meets overcooked in an intense fast-paced action RPG”
2. **Player’s motivation.** What do you want the player to experience and feel? Why would they like to play the game?
3. **The masterpiece.** What does the game look like? What are your game references? Are there any images that convey the idea or sensations in the game? Do you have any mockup or wireframe of the idea? Just paste them here!
4. **Risks and challenges.** What are the drawbacks of the idea? Is there something we don’t know and need to learn? Is the theme already overused?

With the “Lost & Found” theme as our focus point, our objective was to define the basic rules of the game, know where we were gathering references and inspiration, and have a clear path to follow. We were able to flesh out 6 ideas. After detailing them, we did a round of voting (with three votes each) and had a winner: **idea #6**.

![](crush-hour-04|16:9)

### Brainstorming round 2

We realized that we had a strong core game, but we didn’t have any idea what our game would look like. So we started a new Brainstorming round, focusing only on one question: **What can be our game’s theme? Where can it be set?**

![](crush-hour-05|16:9)

Like the previous round, we listed ideas, grouped them, and finally voted for the most promising ones. Since we were running out of time, we decided to go with the most voted idea: **the game would be set at the São Paulo Metro Station.**
:::

:::track Define
### Game design pillars

This method helps the team to fix concepts and ideas about the game, grounding the global game design from the start. It helps the team to make accurate decisions, produce a cohesive design, and avoid failures.

In our design, we found pictures and addressed the YES / NOs for four pillars: **Chaos / Overwhelm**, **Rhythm / Pressure**, **Metro**, and **Storytelling / Emotion**.

![](crush-hour-06|16:9)

This step allowed us to come up with the basic narrative of the game: you work at the Crush Booth, a service offered by the Metro to help their passengers find their lost crush. You’ll receive descriptions of the crush and assemble them to deliver a picture of the lost crush to the passenger.

### Basic mechanics

After defining our pillars and basic narrative, we translated our game idea into the minimum possible mechanic loop, understanding how many areas we needed to work on. In our case there were three:

- **Narrative.** To understand the Player’s goals and NPCs’ motivation
- **Organization.** What information the Player will receive and work with
- **Match.** The main goal of the game

![](crush-hour-07|16:9)

Our basic game loop is:

1. The NPC has a crush, needs to find it, and describes the physical appearance of the crush to the Player
2. The Player assembles the composite sketch and delivers the print of the sketch to the NPC
3. The NPC reacts positively or negatively to the sketch

Here we decided that the people’s description mechanic would be based on 8 categories: hair, eyebrows, beard, shape, nose, eyes, mouth and detail. The categories of hair, beard, eyes, and face have up to five **color** variations, and all categories have four to five **style** variations. This way we were able to have more than **1000 combinations of faces!**

### Visual references

We also spent some time searching for visual references that could guide us when making the User Interface and Character Design.

![User interface and mood.](crush-hour-08|4:3)
![Modular characters.](crush-hour-09|4:3)

### System interface wireframes

Our next step was to brainstorm some possible ways to show the game commands and information to our Players. We imagined two possible approaches:

1. **Breaking the 4th wall.** The Player is working for Crush Booth and is behind a desk, looking at a line of customers and her computer, where she can assemble the NPC’s description request. Under the desk it is possible to select words and phrases to talk to the NPCs if needed (e.g. asking for more information).
2. The Player controls a character that works for Crush Booth. On the Left, you see the character’s workstation, the metro environment, and people gathering around the desk. The Player can select the NPC to interact with and other items such as the Computer and the Printer. On the Right, you have an interactive area where the Player sees the selected element on the Left which can be an NPC, the Computer screen, or the Printer.

![Option 1](crush-hour-10|4:3)
![Option 2](crush-hour-11|4:3)

We decided to go with the second option because it felt more interesting to show the booth in the metro station, with more space to work with the background and other illustration assets. Since we were short on time, at this point our artist started to work on the NPCs’ assets and facial modules.
:::

:::track Planning
After Discovering and Defining, it was time to plan the full loop of our game. We started by creating a detailed Player Flow, mapping the player’s actions and the feedback she would receive from the game. With the Player Flow, we were able to define:

- What kind of interface we were going to show
- Rhythm of the game
- Win and Lose conditions
- Point calculation
- Key moments for sound and visual feedback

![The Player Flow.](crush-hour-12|16:9)

One last flow to improve our game feel was the Rhythm Flow. Here we sorted what happens in each minute of the game by stating how many NPCs appear over time and when the rush hour would take place.

![The Rhythm Flow.](crush-hour-13|16:9)

The variables we found were:

- Time the NPC would wait at the booth for the photo
- Time between the NPCs showing up
- Time when the Rush Hour would start

After the first part of the prototype was done, we playtested to tune the pacing of the Rhythm Flow.
:::

:::track Production
After defining our game loop and the overall feel of the game, each team member started the Production, working on their tasks: code, narrative, illustration and UX/UI. Other important areas were playtest, music, sound FX and extra art.

### Art

![NPCs illustration and animation.](crush-hour-14|16:9)
![](crush-hour-15|16:9)
![](crush-hour-16|16:9)

![Some facial assets.](crush-hour-17|16:9)

### Narrative

The screenwriter focused on the narrative mechanics and logic, finding a way that could be easily implemented in the game.

![](crush-hour-18|16:9)

Besides that challenge, we faced the problem of how to name skin tones: as humans we are diverse, and some words could sound wrong or disrespectful. After some brainstorming we found our way around and decided to go with: “is a bit pale / is light-skinned / is olive-skinned / is dark-skinned”.

### UX/UI

I started with early studies, then improved them. The final version is the one at the top of this page.

![Early studies.](crush-hour-19|4:3)
![Improvements.](crush-hour-20|4:3)

### Coding

Using Unity, the developers were constantly sharing their progress and getting input on their work.

![](crush-hour-22|4:3)
![](crush-hour-23|4:3)

### Sound and music

A friend outside of the group composed the **main music** for our game, with a variation for our three key moments: intro and tutorial, calm time, and rush hour. The **sound FX** we found online at [opengameart.org](https://opengameart.org/) and [freesound.org](https://freesound.org/).

### Logo

I searched for seven different fonts so the team could be part of the choice of our game’s logo style.

![](crush-hour-24|16:9)

We decided to go with option 1, which gave us the feeling of movement and rush. From that choice, I proposed two different designs:

![](crush-hour-25|16:9)
![](crush-hour-26|16:9)

The second design was an attempt to bring the “pun intended” to our game, mixing Crush and Rush, so we agreed to go in that direction. To give it more personality, I added some lines in the big C to bring even more movement, and a heart to translate the crush part. This is our final design:

![](crush-hour-27|16:9)
:::

### Credits

**GGJ official team.** Bruno Luvizotto, Fernanda Nunes, Gustavo Andrade, Marina Pasetchny and Rodrigo Caitano.

**Special thanks.** Nil Simsek (music and sound design), Pedro Camara (game design) and Sampa Diversa (GGJ organization).
