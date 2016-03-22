# story-teller

Story telling dice game written in Python. 

# Introduce

Simple Storyteller dice game that get the idea from Rory's Story Cubes.
You simply choose number of dice's to throw and tell a story and use the
word's that the game give's you.

This is also simple tutorial to start learning python and create a
simple game.

# Requirements

* Python 3.4
* Basic understanding of programming

# How to start the game

Simply type `python story-teller.py`
or if you have installed Python2 you may have to start the game with
`python3 story-teller.py`

# Tutorial

In this section the code is explained for better understanding.

### Beginning
First you need to import some classes to get proper functionality to the program

```python
import random
import time
import sys
```

Second you can introduce the array witch contains the numbers corresponding each
side of a dice (it's simpler to just add all the dice's to a single array so just
add the dice's like first dice is numbers 1-6, second 7-12, third 13-18 and so on)

```python
dices = {1: "Ladders", 2: "Submarine", 3: "Question mark", 4: "World", 5: "Food", 
        6: "Scale of Justice", 7: "Snake", 8: "Necklace", 9: "Fire", 10: "Altar", 
        11: "Rainbow", 12: "Theater", 13: "Clock/Time", 14: "Medicine", 
        15: "Mountains", 16: "Backpack", 17: "Looking Glass", 18: "Bridge",
        19: "Viking Helmet", 20: "Confused", 21: "Elephant", 22: "Rain", 
        23: "Shield", 24: "Beans", 25: "Sunrise", 26: "Treasure Chest", 
        27: "Bang", 28: "Painting", 29: "Bird", 30: "Cauldron", 31: "Gears", 
        32: "Octopus", 33: "Stormy Sea", 34: "Whip!", 35: "Tent", 
        36: "Treasure Map"}
```

So if you type `print(dices[1])` you will get answer: `Ladders`

Pretty simple...

### Logic for the game


### Conclusion

# License

MIT
