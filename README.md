 
# Alien Invasion Game

Alien invasion is a clone of popular arcade game with same name with the help from the book "Python crash course" 

![Image of game](https://github.com/jenlcmc/Alien_Invasion/blob/master/images/Screen%20Shot%202021-07-28%20at%208.49.38%20PM.png)

# Introduction

In Alien Invasion, the player controls a ship that appears at the bottom center of the screen + move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the aliens. If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.

In addition, there will be 3 levels for player to chooses, from easy to hard. To choose, click the level and click play. Each level will have different speed and different bullets limit.

# Requeriments

- Python 3.0 +
- Pygame
- Sound packages (optional) 

## To install, please follow the office guide to install python 
**To install pyagme**
```$ pip3 install pygame```

**To install sound packages + pygame (MacOS)/ Supposed that python install via brew**
```
$ pip3 install pygame
$ brew install hg sdl sdl_image sdl_ttf
$ brew install sdl_mixer portmidi
 ```
 
 **To install sound packages + pygame (Windows)**
```
$ pip3 install pygame
 ```
 **There is a problem with sound packages for windows, so if it not work, please comment out following lines in alien_invasion.py file**
 - 16
 - 207
 - 229
 - 289


# To play
```$$ python3 alien_invasion.py```
# Controls

* Space-bar
  * Shoot
* Arrows keys (left - right)
  * Move the ship left / right
* q
  * to quit the game/exit fullscreen

# Play
```Please clone the respitory and cd to the folder ```

**There is few sub games that the player can try**

```cd into that folder```

```$ python3 game.py```

# Running

```$ cd src ```

```$ python3 alien_invasion.py```

**There is another file that automate the ship if the player want to try**

```$ python3 ai.py```

The player will have to choose the level same way with the above instruction

**Enjoy!**

# Upcoming features
- Add health bar for ship
- Make aliens shoot the ship
- Add shield for ship 
