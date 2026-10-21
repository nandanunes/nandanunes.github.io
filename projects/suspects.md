*Suspects Mystery Mansion is a free-to-play multiplayer deduction game that uses Zooba IP, setting their characters in a mysterious mansion to solve a murder.*

![In-game preview of the new Main Menu. The characters are indeed distracting, but the hierarchy is clearer.](suspects-03|16:9)

## Overview

I joined the **Suspects Mystery Mansion** team as a **UX Designer**, responsible for improving the gameplay experience and designing all social and metagame features.

The game was fully developed in **five months**, and I joined starting from the second month. After the Global launch, I led the UX for monetization and social features. It had a soft launch in Brazil and other Latin countries in March 2021, and the Global Launch was on April 21st, 2021. Until that date it had almost **10 million downloads worldwide**.

You can [watch the launch trailer](https://www.youtube.com/watch?v=T0WshMp9wOU) or download the game for [Android](https://play.google.com/store/apps/details?id=com.wildlifestudios.free.online.games.suspects&hl=en&gl=US) and [iOS](https://apps.apple.com/ai/app/suspects-mystery-mansion/id1546088542#?platform=iphone). A Steam version is coming soon.

### What I did

- Benchmarking the main references for the upcoming features
- Planning and conducting workshops within the team to plan new features and remove design or product barriers
- Prototyping screens and interactions using Figma and Principle
- Designing the whole Metagame loop and its main features and flows such as Battle Pass and Match Results Screen
- Designing and improving social features such as friends list, voice chat, referral program, game lobby, and more
- Planning and conducting playtest sessions with players
- Tuning and improving some UX aspects of the gameplay for our players such as clarifying in-game roles, understanding their goals, and having a better first-time user experience (FTUE)
- Following the soft launch reception, observing FTUE from streamers and collecting feedback from users in our official Discord Channel

## Main Menu Revamp

Suspects was a game made by a very small team. Many of its design decisions were made on the go, and the Main Menu screen had to fit all the new features and options that were being added to the game during development. After the Global Launch, we dedicated time to reevaluate it, since it’s one of the most important screens of the game: the hub where the Player accesses all the core features.

The problem we set out to solve: **“The Main Menu is cluttered and busy, lacking hierarchy and contrast.”**

### The result

![Before: the Main Menu during Global Launch, a total mess!](suspects-11|2:1)
![After: a lot of space and a unified visual identity.](suspects-12|2:1)

The revamp was well received by our players, with positive evidence from streamers and metrics.

- **Players’ impression.** YouTubers and streamers reacted to the new menu positively, with comments like “Now this game feels very premium” and “I like to see that I have friends online without having to click on a button”
- **Metrics and performance.** I can’t disclose the full metrics, but we had an **increase in retention**, more clicks on Store and Friends, and our Players were more eager to play with Friends

### How I got there

Select a step to read more about it:

:::tracks
Understanding the problem | Pain points, constraints, goals and how we would measure success
Benchmark | What other multiplayer games do with their main menu
Wireframes | Three options, their strengths and weaknesses
Next steps | What is left to improve
:::

:::track Understanding the problem
Through a **workshop with the game’s stakeholders** (Game Director, Game Designer, UI Engineer, Visual Designer, and Project Manager) we discussed and gathered information on what were the main problems with the screen and what constraints we would have. We also collected data on how our Players use and interact with the current Main Menu, and decided to go with quantitative data such as most clicks and retention. Then we defined metrics to compare before and after the revamp.

### Main concerns

- No First Time User Experience (FTUE) – The Main Menu is the same for all players, doesn’t matter the stage they’re in the game they always see everything that is available
- No hierarchy – everything feels important at the same time
- Hard to read all the information – lack of contrast and font sizing
- Visual inconsistency – too many styles and sizes
- Lack of affordance – no cue of what is clickable and the expected outcome
- Display of options that are rarely clicked by the Players (telemetry data)
- No more space on the screen to add future events or offers

### Constraints

- The character collection should be kept in the background due to the complexity of changing it from both engineering and design perspectives
- We can’t solve FTUE before the UX/UI revamp – the noise the menu causes now could affect the process of calibrating the FTUE

### Priorities

Based on that, we observed two main areas that needed attention:

1. **Revamp visual design and improve usability (UX/UI) ← priority**
2. Design and implement FTUE based on player journey ← TBD after the visual revamp

### Design objectives

- Improve the usage of space on the screen, making better use of negative space
- Create a clear hierarchy between buttons and elements
- Group elements by function and importance
- Hide less important options and features
- Have dedicated space for future Live Ops events

To measure the success of the revamp, we followed and compared metrics such as retention, store clicks, time to start match, and time spent on the menu.
:::

:::track Benchmark
When selecting the games, the references followed one criterion: **“Landscape mobile multiplayer games with focus on social features.”** The options were categorized by similar layout, considering the Play button position and how they organize menu options (left, left and right, center).

![Some of the Main Menu screens gathered for the study. Among them were Brawl Stars, Wild Rift, Asphalt, and COD Mobile.](suspects-04|16:9)

After that, I selected two games that were more aligned with Suspects’ product vision (cartoonish fantasy theme, heavily social, monetization on Battle Passes and cosmetics) and went deep into analyzing their menu structure. The games were Brawl Stars and Wild Rift.

### Thumb zone

Mapping what elements and areas of the screen are out of the reach of thumbs.

![](suspects-05|16:9)

### Hierarchy

Understanding and defining the order of importance of each element or area, considering its size and contrast among other elements and background.

![](suspects-06|16:9)

### Functionality

Mapping what each button does, how they’re grouped, and what kind of information is displayed on screen. From this study, I concluded that both games divide and organize their screen in two parts:

- **Individual.** Everything that tracks the Player’s progress or depends only on the Player herself to be accomplished (player level, character level, character collection, battle pass, rewards) and single actions (store)
- **Social.** Everything related to playing the game or managing social features (play matches, friends, gameplay events, club or clan, chat)

![](suspects-07|16:9)
:::

:::track Wireframes
When doing the wireframes, I kept in mind the following aspects:

1. **Benchmarked examples structure.** When organizing the elements on the screen, I followed the logic of having the Player (individual) features on the left and the Social ones on the right.
2. **Improve our menu interactions based on benchmark.** Our Friends list was a Drawer activated by a button – not very intuitive but better than creating a new screen. In Wild Rift, they also use the drawer format but with more clarity which is an interactive drawer, giving extra information on what friends are online or not on the go.
3. **Hierarchy and contrast.** This aspect should be very clear in the wireframe so the Visual Designer can understand the importance of light in this context.

After sketching some options, I showed them to the game team and the UX team so they could give their feedback on each version. With that data in hand, I made some adjustments to the designs and highlighted the **strengths** and **weaknesses** of each one.

Unfortunately we couldn’t test the options with players due to time constraints. Not ideal, but with the time I had, I was able to collect feedback from other UXers and Researchers from the UX department.

### Option A

![A balanced mix between Brawl Stars and Wild Rift.](suspects-08|16:9)

**Strengths**

- Improved button grouping, hiding less relevant options inside menus or reducing them to iconography
- Clearer distinction between the Background (collection) and the Foreground (buttons)
- Space to add Live Ops elements

**Weaknesses**

- When a Player has all characters, their animation can be distracting
- We still have some elements competing for attention on screen

### Option B

![An option leaning more towards Wild Rift.](suspects-09|16:9)

**Strengths**

- Keeps most of the options within reach by using the bottom portion of the screen
- Clearer distinction between the Background (collection) and the Foreground (buttons)
- Space to add Live Ops elements

**Weaknesses**

- When a Player has all characters, their animation can be distracting
- Because of the buttons at the bottom, there is less negative space, so it can feel a little claustrophobic

### Option C (the extra one)

![We did it anyway.](suspects-10|16:9)

**Strengths**

- Reduces all extra information into buttons on the left portion of the screen
- Focuses on the Player’s favorite character, with the possibility to add thematic backgrounds
- A lot of extra and negative space

**Weaknesses**

- The Player doesn’t have an idea of her character collection
- It would be hard for engineering to change to this version
- The design would need other screens and flows for character collection and cosmetics management

Even though option C looked the best design-wise, we decided to start the visual explorations with option A, since it is the version with the fewest weaknesses, considering engineering constraints back then. We understood that the Main Menu would be further iterated to reach the most promising version in the future.

The final visual design was done by Claudio Watabe.
:::

:::track Next steps
- Get feedback from players in deep listening sessions to collect precise data on what can be further improved in the game
- Reflect on the revamp to other screens (when possible) and study what other elements can also receive a better visual treatment
- Keep following the metrics to understand what other areas of the menu are causing friction for our Players
:::
