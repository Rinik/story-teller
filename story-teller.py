#!/usr/bin/env python3

# import needed classes, random to scramble the dices, time to add waiting time when the dice's are rolled.
import random
import time

# Created Array of dice's number equals one side of the dice. So 1-6 is the first dice, 7-12 second and so one.
dices = {1: "Ladders", 2: "Submarine", 3: "Question mark", 4: "World", 5: "Food", 6: "Scale of Justice", 
        7: "Snake", 8: "Necklace", 9: "Fire", 10: "Altar", 11: "Rainbow", 12: "Theater",
        13: "Clock/Time", 14: "Medicine", 15: "Mountains", 16: "Backpack", 17: "Looking Glass", 18: "Bridge",
        19: "Viking Helmet", 20: "Confused", 21: "Elephant", 22: "Rain", 23: "Shield", 24: "Beans",
        25: "Sunrise", 26: "Treasure Chest", 27: "Bang", 28: "Painting", 29: "Bird", 30: "Cauldron",
        31: "Gears", 32: "Octopus", 33: "Stormy Sea", 34: "Whip!", 35: "Tent", 36: "Treasure Map"}

# The main function, does just start the game.
def main():
  while game():
    pass

# The Game function. Randomizes the dice's.
def game():
  print("Let's start the story-teller...")
  # Choose the number of dice's to throw
  player = choose()
  # Throw each dice
  dice_one = random.randint(1,6)
  dice_two = random.randint(7,12)
  dice_three = random.randint(13,18)
  dice_four = random.randint(19,24)
  dice_five = random.randint(25,30)
  dice_six = random.randint(31,26)
  # Add dice's to array and shuffle the dice's in that array
  all_dices = [dice_one, dice_two, dice_three, dice_four, dice_five, dice_six]
  random.shuffle(all_dices)
  # Give the result for the dice rolling.
  result(player, all_dices)
  return again()

# Choose function to choose number of dices to throw.
def choose():
  while True:
    player = input("How many dice you would like to throw? 1-6: ")
    try:
      player = int(player)
        if player in range(1,6):
          return player
        except ValueError:
          pass
        print("Oops! Try again. Please enter number between 1 and 6.")

# Result function get's the values from the game function and returns the result
def result(player, all_dices)
  print("Throwing...\n")
  time.sleep(1)
  print(".... the dice(s)\n")
  time.sleep(1.5)
  print("The dice(s) are: \n")
  for dice_number in all_dices[:player]:
    print(dices[dice_number]+"\n")

# Again function is simple asking funtion to play again
def again():
  answer = input("Would you like to throw again? y/n: ")
    if answer in("y", "Y", "yes", "Yes", "YES")
      return answer
    else:
      print("Thank you for playin! See you next time.")

# if the program is started straight from the file, then run the game.
if __name__ == "__main__":
  main()
