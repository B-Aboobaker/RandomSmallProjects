import random

randomNumbers = []
userGuesses = []
correct = 0

for num in range(0, 3):
    randomInt = random.randint(1,9)
    randomNumbers.append(randomInt)

firstGuess = int(input("Please enter your first guess: \n"))
if firstGuess in randomNumbers:
    correct += 1
userGuesses.append(firstGuess)

secondGuess =int(input("Please enter your second guess: \n"))
if secondGuess in randomNumbers:
    correct += 1
userGuesses.append(secondGuess)

thirdGuess = int(input("Please enter your third and final guess: \n"))
if thirdGuess in randomNumbers:
    correct += 1
userGuesses.append(thirdGuess)

print("User Guesses: ", * userGuesses, sep='   ')
print("Random Numbers: ", * randomNumbers, sep='   ')

if correct == 0:
    print("You have not won anything.")
elif correct == 1:
    print("You have won: $10")
elif correct == 2:
    print("You have won: $100")
elif correct == 3:
    print("You have won: $1,000")
elif firstGuess == randomNumbers[0] and secondGuess == randomNumbers[1] and thirdGuess == randomNumbers[2]:
    print("You have won: 1,000,000")

