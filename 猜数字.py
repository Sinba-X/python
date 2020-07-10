# This is a guess the number name
import random
secretNumber = random.randint(1,20)
print('i an thinking a number between 1 and 20')

# ask thr player to guess 6 times
for gussesTaken in range(1,7):
    print('take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break
if guess == secretNumber:
    print('Good job! You guessed my number in '+str(gussesTaken)+' guesses!')
else:
    print('Nope! The number i was thinking of was ' + str(secretNumber))
