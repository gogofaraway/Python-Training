### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, LetterInWord, LetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not LetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background

   if(LetterInCorrectPlace):
     print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
   else:
     print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if letter in actual:

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
  
       printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
     printColorfulLetter(letter, False)
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# TO-DO: Write a Function that takes in a six-lettered word from the user
def inputSixLetterWord():
  word = ""
  while len(word)!=6:  
   word = input("Enter a six letter word: ")
  return word  
#This marks the end of the function definitions, below this is where the program will actually start!
### Main Program ###

# TO-DO: Write the logic of the game here!
# Create a variable to hold the user's guess as a dummy value
userGuess = ""
#create a secret word
secret = "paddle"
#track how many times the user tried
tries = 0
#Repear the game until the user guesses correctly
while (secret != userGuess and tries <5):
#Ask the users to enter a six letter word
 userGuess = inputSixLetterWord()
#Disply the six letter word and show color for each word
printGuessAccuracy(userGuess, secret)
print()
tries +=1
#disply whether if the user wins or loses
if(userGuess == secret):
  print("YOU WIN!")
else:
  print("YOU LOSE")