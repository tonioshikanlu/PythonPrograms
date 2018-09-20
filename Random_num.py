import random

print ('Hell0. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20. Guess.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1,7):
	print ('Take a guess.')
	guess = int(input())

	if guess < secretNumber:
		print('Too low.')
	elif guess > secretNumber:
		print ('Too high.')
	else:
		break # Condition for correct guess

if guess == secretNumber:
	print('Good Job, you guessed correct in ' + str(guessesTaken) + ' guesses.')
else:
	print('I was thinking of '+ str(guess))