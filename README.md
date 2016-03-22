# story-teller

Story telling dice game written in Python. 

# Introduction

Simple Storyteller dice game that get the idea from [Rory's Story Cubes](https://www.storycubes.com/ "Rory's Story Cubes").
You simply choose number of dice's to throw and tell a story and use the
word's that the game give's you.

This is also simple tutorial to start learning python and create a
simple game.

# Requirements

* Python 3.4
* Basic understanding of programming

# How to start the game

Simply type `python story-teller.py` or if you have also Python2
you may have to start the game with `python3 story-teller.py`

# Tutorial

In this section the code is explained for better understanding.

### Beginning
First you need to import some classes to get proper functionality to the program

```python
import random
import time
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

Next most important step is to start the program, there is actually two parts of this.
Fist make `if` statement that check if the code is run straight from the commandline.
The statement checks that the `__name__` attribute is named `__main__` what happens
if you run the code with `python story-teller.py`, and if the statement is true then
it runs `main()`.

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
`game()` function. First of all the function prints out the Welcome message and then
asks player to choose the number of dices with the `choose()` function. Then the
program generate random number for each "dice" from the range that is given. So the
`dice_one` could have value from 1 to 6, the dice_two from 7 to 12 and so on. Then the
dice's are stored in `all_dices` list and the list is then shuffled. So you never know
what dice's you came up when you throw less than all the dice's. Then program calls
the `result()` function with parameters `player` and `all_dices` to show the result of
the thrown dice's and finally asks user to play again or quit the program.

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


The `choose()` function is simple ask function to just ask the user to enter the
number of the dice's witch user want to throw. The `input` function reads the users
value from the keyboard. Then the value is try catched to `int` value. If the `try`
method is failed, the Error prompt is showed and user is asked to re-enter the
correct value. Basically the program can be done without try catch but if the user
enters wrong value the program quits with error message (and thats not good).

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
        print("Oops! Try again. Please enter number between 1 and 6.")
```


The `result` function needs two values, `player` value witch is the `int` value of
the thrown dice's. Second value is `all_dices` value witch includes the shuffled
`list` of the thrown dice's. For example if the player has chosen to throw 2
dice's the passed values could be like `result(2, [16, 4, 22, 34, 26, 10])`.
After that there is printed message to user and `time.sleep()` when the program
holds out for the given time and then print's out the result. The `for` loop is
constructed so that the loop is looping just so many times as the player has
entered the number of dice's. So in our example the `for` loop is constructed
like so `for i in all_dices[2]:`, and the first result would be `16` and second
result would be `4`. So if we like to print out the result in our `dices` array
the result would be `Backpack` and `World`.

```python
def result(player, all_dices):
    print("Throwing ...\n")
    time.sleep(1)
    print("... the dice(s)\n")
    time.sleep(1.5)
    print("The dice(s) are: \n")
    # For loop that show's just the first dice's to the chosen number of dices (player) = choice
    # if you want to show the rest of the dice's just do another for loop and change the [:player] to [player:]
    for i in all_dices[:player]:
        print(dices[i] + "\n")
```


Last the`game()` function calls the `again()` function where the program prints
out would you like to play again or not. If the answer is some of the valid
answers the program starts over, but if it's not the program quits.

```python
def again():
    answer = input("Would you like to throw again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "YES"):
        return answer
    else:
        print("Thank you for playing! See you next time.")

```
### Conclusion

This is really simple game program but introduces lot of logic in code. So feel free to tinker and try out.

# License

MIT
