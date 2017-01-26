import random
magicNumber = random.randint(1,20)
print ('I am thinking of a number between 1 and 20. \n' + 'What is it?')
for guessesTaken in range(1, 7):
    print('Take a guess.\n')
    guess = int(input())
    print ('')
    if guess > magicNumber:
       print ('You guessed a little higher. \n')
    elif guess < magicNumber:
        print ('You guessed a little lower. \n')
    elif guess == magicNumber:
        print ('You got it correct, it was \n ', magicNumber)
        break
    if guessesTaken > 5:
        print('Sorry, the limit is up, the number was ', magicNumber)
