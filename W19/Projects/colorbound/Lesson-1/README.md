# Meet-Up #1 Agenda:

**Objective**: Learn about game loops, how to handle input, and learn how to draw graphics using HTML5 canvas.

Please sign up for the general slack at uwcoffeencode.slack.com if you haven't already.

## 1. Tools
* If you haven't already, I would recommend you install a text editor
* Google chrome

## 2. Colorbound
* A 2d singleplayer shooter platformer game written in a custom engine.

## 3. Basics

### The Game Loop
Games, unlike most other types of software, must continue working even if the user doesn't provide any new input.
Furthermore, they must present their work frequently and steadily in order to give the appearance
of smooth animation.

Generally speaking, one unit of work for the game consists of the following:
1. Processing user input
2. Performing game logic
3. Presenting the game

This describes the high-level anatomy of a single "frame" of a game; the game loop is responsible for running
this sequence frequently and steadily.

As mentioned earlier, games differ from other types of software in that they don't wait on user input in that
first step. As such, a niave loop such as the following:

```js
while(true) {
    processInput();
    update();
    draw();
}
```

will simply 

### Input Handling in HTML5

### Drawing Images using Canvas
