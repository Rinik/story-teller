# story-teller

A story telling dice game written in Python.

# Introduction

This is a simple Storyteller dice game that got its idea from
[Rory's Story Cubes](https://www.storycubes.com/ "Rory's Story Cubes").
Just simply choose a number of dice to throw and tell a story using the words
that the game gives you.

This is also works as a simple tutorial to start learning python and to create a
simple game.

# Requirements

* Python 3.4
* Basic understanding of programming

# How to start the game

Simply type `python story-teller.py` or if you also have Python2,
you may have to start the game with `python3 story-teller.py`

# Tutorial

In this section the code is explained to provide better understanding.

### Beginning

First you need to import some classes to get proper functionality to the program

```python
import random
import time
import sys
```

Second you can introduce the array, which contains the numbers corresponding to
each side of a die (it's simpler to just add all the dice to a single array, so
just add the dice like the first die is numbers 1-6, the second 7-12, the third
13-18 and so on)

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

Then there is class `BColors` what is for colouring text. So if you want to print
text in red you just need to add `BColors.FAIL` to your print function and don't
forget to restore the color after the line of text with `BColors.ENDC`.

```python
class BColors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
```

Next the most important step is to start the program. There are actually two parts to this.
First make an `if` statement that checks if the code is run straight from the commandline.
The statement checks that the `__name__` attribute is named `__main__`, what happens if you
run the code with `python story-teller.py`, and if the statement is true then it runs
`main()`.


```python
if __name__ == "__main__":
    main()
```

Then the `main()` function runs `game()` function as long as `while` loop is `true`.

```python
def main():
    while game():
        pass
```


### Logic for the game

So here is the main logic for the whole game in these 4 functions. So let's start with
the `game()` function. First of all, the function prints out the Welcome message and then
asks the player to choose the number of dice with the `choose()` function. Then the
program generates random number for each "dice" from the range that is given. So the
`dice_one` could have a value from 1 to 6, the `dice_two` from 7 to 12 and so on. Then the
dice are stored in `all_dices` list and the list is then shuffled. So you never know
which dice you come up with when you throw less than all of the dice. Then program
calls the `result()` function with parameters `player` and `all_dices` to show the
result of the thrown dice and finally asks the user to play again or quit the program.

```python
def game():
    print("Let's start the story-teller...")
    player = choose()
    dice_one = random.randint(1, 6)
    dice_two = random.randint(7, 12)
    dice_three = random.randint(13, 18)
    dice_four = random.randint(19, 24)
    dice_five = random.randint(25, 30)
    dice_six = random.randint(31, 36)
    all_dices = [dice_one, dice_two, dice_three, dice_four, dice_five, dice_six]
    random.shuffle(all_dices)
    # Give the result for the dice rolling.
    result(player, all_dices)
    return again()
```

The `choose()` function is a simple ask function to just ask the user to enter the
number of the dice that the user wants to throw. The `input` function reads the users
value from the keyboard. Then the value is try catched to the `int` value. If the
`try` method fails, the Error prompt is shown and the user is asked to re-enter
the correct value. Basically the program can be done without try catch but if the
user enters wrong a value the program quits with an error message (and that's not good).

```python
def choose():
    while True:
        player = input("How many dice you would like to throw? 1-6: ")
        try:
            player = int(player)
            if player in range(1, 7):
                return player
        except ValueError:
            pass
        print(BColors.FAIL+"Oops! Try again. Please enter number between 1 and 6."+BColors.ENDC)
```

The `result` function needs two values, the `player` value witch is the `int` value of
the thrown dice. The second value is `all_dices` value, which includes the shuffled
`list` of all the thrown dice. For example if the player has chosen to throw 2 dice
the passed values could be `result(2, [16, 4, 22, 34, 26, 10])`. After that there is
a printed message to user and `time.sleep()` where the program holds out for the given
time and then prints out the result. The `for` loop is constructed so that the loop
is looping just the same amount of times as the number of dice entered by the player.
So in our example the `for` loop is constructed as `for i in all_dices[2]:`, and the
first result would be `16` and second result would be `4`. So if we'd like to print
out the result in our dices array the result would be `Backpack` and `World`.

```python
def result(player, all_dices):
    throw_text = "Throwing . . . "
    for l in throw_text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(0.5)
    print("Dices!\n")
    time.sleep(1.5)
    print(BColors.OKBLUE+"The dice(s) are: \n"+BColors.ENDC)
    for i in all_dices[:player]:
        print(BColors.OKGREEN+dices[i] + "\n"+BColors.ENDC)
```

Finally the `game()` function calls the `again()` function where the program
prints "out would you like to play again or not." If the answer is one of
the valid answers the program starts over, but if it's not, the program quits.

```python
def again():
    answer = input("Would you like to throw again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "YES"):
        return answer
    else:
        print("Thank you for playing! See you next time.")

```
### Conclusion

This is a really simple game program but introduces lot of logic in code. So feel free to tinker and try it out.

# License

MIT
