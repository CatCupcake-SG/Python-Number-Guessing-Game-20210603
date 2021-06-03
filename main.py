#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
from replit import clear

EASY_LEVEL = 10
HARD_LEVEL = 5

#start
def start():
  print(logo)
  print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
     
  
  def option():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy" :
      #return 10 --original code--
      return EASY_LEVEL #instead of using number. set a global var will makes it dynamic
    else:
      #return 5  --original code--
      return HARD_LEVEL 
  
  attempts = option()
  number = random.randint(1,100)
  game_over = False
  
  #play
  while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    
    if guess > number:
      print("Too high.") 
    elif guess < number:
      print("Too low.")
    else:
      game_over = True
      print(f"You got it. The answer is {guess}.")

    if attempts == 0:
      game_over = True
      print(f"You have run out of guesses. The answer is {number}.")
    elif attempts !=0 and not game_over :
      print("Guess again.")
       
    

    

while input("Do you want to play a game of Number Guessing? Type 'y' or 'n': ") =='y' :
  clear()
  start()  



