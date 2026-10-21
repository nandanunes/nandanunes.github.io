*Angry Birds Friends is a competitive slingshot game that combines puzzles and tournaments, offering new levels every week for the past 10 years!*

![](angry-birds-friends-hero|16:9)

## Overview

Angry Birds Friends levels got bigger and more complex with time, with new blocks, mechanics, camera zoom and intricate puzzles. Even though Angry Birds is a classic, some blocks’ design became outdated, and their visuals weren’t good enough to keep up with the evolution and communicate their behavior and intent.

In this case study, we will see the UX improvement process for the Trigger pack: the Trigger, the Wires, the Landmine and the Sign. Select a step to read more about it:

:::tracks
Context | Understanding how the block works and how it’s used
Research | Benchmarking other games for Trigger references
Design | Writing the requirements and developing options
Playtest | Collecting feedback and iterating
Guidelines | Unifying how Level Designers should use the new pack
:::

:::track Context
The Trigger block was composed of two blocks:

![](angry-birds-friends-context-01|16:5)

- A control panel, a rectangular block that resembles a metal panel with buttons
- A small light switch, only available in the color [add the color here]

Triggers are used in levels to gate areas or effects. They had to be hit by the Player with a bird or block in order to get activated. The effects would vary from opening enclosed level areas to making blocks fall off-screen or activating explosives.

There were many instances where the Triggers were used without following guidelines and uniformity within levels, in ways that would confuse Players trying to make sense of the level puzzles.

![](angry-birds-friends-context-02|16:5)

The main pain points of Triggers were the following:

- The control panel + light combo is small and hard to see in smaller screens
- There was no clear way to communicate to the player what a trigger could do
- It can be hard to associate the Trigger with other level mechanics, only using pieces of material to hint at that (they were too small and subtle to be used as a pattern)
- It’s not part of the Player’s decision making process when solving the puzzle
    - It’s hard to understand what the trigger is connected to when on-screen
    - It’s not clear what the trigger will do when off-screen
- There is no convention in how they’re used by Level Designers
    - Some triggers have hints, some don’t
:::

:::track Research
Before sketching anything, I looked at how other games handle triggers, wires and visual hints. I started with the classics, from Super Mario to indie hits like Terraria, and kept a short note on what each one does well and what I could borrow for Angry Birds Friends.

### Triggers and wires

#### Super Mario World
![The blue P-Switch.](abf-research-mario-world-1|4:3)
![The yellow “!” Switch.](abf-research-mario-world-2|4:3)
Each switch is recognizable at a glance, by color and by one clear symbol. The color also links the switch to the blocks it activates.

#### Super Mario Wonder
![A red dome button with a Bowser emblem.](abf-research-mario-wonder-1|16:9)
![The Bowser machine.](abf-research-mario-wonder-2|16:9)
A red dome button, just like ours, but with an emblem that tells you what it is connected to. Same shape, one extra piece of information.

#### Terraria
![Detonator, lever and colored wires.](abf-research-terraria-1|4:3)
![Colored wires connecting triggers to devices.](abf-research-terraria-2|16:9)
Colored wires make it easy to follow which trigger is connected to which device. Detonators and levers look different, so each one already hints at what it does.

#### Oxygen Not Included
![Weight plate](abf-research-oni-plate|4:3)
![Signal switch](abf-research-oni-switch|4:3)
![Timer sensor](abf-research-oni-sensor|4:3)
The trigger shows its own state. The weight plate changes color when it is activated, the switch changes shape and color, and the sensor moves a pointer and lights up in the color that was activated. The feedback is part of the object.

### Extra: signs

While looking at triggers, I found that signs can hint at what a trigger will do before the player uses it. These were the best examples.

#### Real-life warning signs
![Warning signs: falling rocks, explosion, fireworks, fire and wind.](abf-research-signs-irl)
One pictogram says what to expect, with almost no reading. People recognize them instantly.

#### Portal
![The test chamber info sign.](abf-research-portal-1|4:3)
![The pictograms for the testing elements.](abf-research-portal-2|4:3)
The test chamber sign tells the player which chamber they are entering, how many there are in total, and which testing elements to expect. It helps the player understand what puzzle awaits in the next stage.

#### Dead Cells
![A sign before a door, warning what awaits.](abf-research-deadcells-1|16:9)
![A sign on top of a door, showing the combination that opens it.](abf-research-deadcells-2|16:9)
Signs before a door warn the player what is inside, and help them decide where to go. Signs on top of a door show the combination that opens it. Since the player sees them before solving the puzzle, they build expectation.

#### The Pedestrian
![The Pedestrian: post-its with drawings of what is in each direction.](abf-research-pedestrian)
Post-its show what the player will find in each direction. That helps with backtracking while solving the puzzle.

### What I took from this

- Color can connect a trigger to what it affects.
- The object itself should show when it was activated.
- A small sign can hint at the effect without spoiling the surprise. This was the starting point for the info signs I explored in the Design step.

*Images are screenshots of the games mentioned, shown for reference. Sources: Oxygen Not Included Wiki (Weight Plate, Signal Switch, Timer Sensor).*
:::

:::track Design
The research and the problems from the Context step became the requirements for the new Trigger. First, what the Trigger needs to communicate. Then, what it needs to be. Finally, the pack that came out of it.

### What it needs to communicate

The Wireless Trigger needs to inform what it is connected to, or what kind of behavior it is going to play once it is activated. That gives two requirements:

1. **Communicate the connection between a Trigger and its far-away counterpart (on-screen).** Color helps, as the wires in Terraria and the switches in Super Mario show, but color alone was not enough in our levels. A visual sign next to the color can help the Player connect both, when needed.
2. **Anticipate the Trigger behavior without spoiling the surprise (on and off-screen).** Signs in Portal, Dead Cells and real life show that a small pictogram lets people predict what will happen. The Player can then strategize better to solve the puzzle.

### What it needs to be

From the pain points and the references, I wrote six requirements for the Trigger itself:

1. **Stand out from other blocks and give a “poppable feel” like Pigs.** The control panel had no contrast and got lost in the level. Pigs are what players love to pop, so the Trigger should invite a hit in the same way.
2. **Get the Player’s attention.** The Trigger was not part of the Player’s decision making. It needs to be noticed before the first shot, so it becomes part of the plan.
3. **Have a simple but recognizable shape.** On a small screen only a simple silhouette survives. In Terraria, the detonator and the lever are told apart by shape alone.
4. **Have a range of colors to select.** Color is how the references link a trigger to what it affects, and it was missing in our levels.
5. **Have the size of a medium pig.** The old control panel was too small to see on smaller screens. A medium pig is a size players already know and can read at a glance.
6. **Have VFX to show it is active (for example, blinking).** In Oxygen Not Included the object shows its own state, so the Player always knows if it was activated.

### The Trigger pack

The requirements became a pack of four parts that work together:

- **Trigger.** The part the Player hits. It has a simple shape, a range of colors and a blinking light that shows it is active.
- **Wires.** The physical connection between a Trigger and what it activates, in the same color.
- **Landmine.** The wireless counterpart of the Wires. It has the same color code as its Trigger and explodes without a wire, so the color is what links both.
- **Sign.** An optional element, to be used only as a last resort. It is a small pictogram next to the Trigger that hints at the kind of effect, such as an explosion, fireworks, falling things, or a question mark for a surprise.

![](abf-design-01|16:9)
:::

:::track Playtest
I playtested the new Trigger pack internally and collected feedback. Three decisions came out of it:

- **The shape.** We tried several shapes and decided to go with the most Mario-like one.
- **The colors.** We decided on four colors: red, yellow, blue and pink. Green was discarded so it would not be confused with the Pigs.
- **The blinking rate.** We tuned the blinking so the Trigger gets noticed without being too crazy.

![The shapes we tried.](abf-playtest-01|16:9)
:::

:::track Guidelines
![The final Trigger pack: Trigger, Wires, Landmine and Sign.](abf-guidelines-01|16:9)

The final pack has four parts that work together: the Trigger, the Wires, the Landmine and the Sign. It also gave us a reason to rewrite the Level Guidelines for how Level Designers use these blocks in Angry Birds Friends.

I did not want a rigid rulebook. The idea was to hand Level Designers a few rules of thumb and leave room for them to experiment, as long as the intention and the result are still easy for the player to understand.

### Triggers, Wires & Landmines

The main rule is that they must clearly indicate what they activate, even if the outcome itself stays hidden. An off-screen result, for example, does not need to be previewed.

#### Do’s

- Connect to something that needs to be destroyed or activated
- Use the Landmine to indicate its connection to that Trigger
- Match the colors of all parts of the mechanic (Trigger, Wire, Landmine)
:::
