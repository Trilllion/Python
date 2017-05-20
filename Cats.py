print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('You have a lot of cats')
    elif int(numCats) < 0:
        print ('You are not from this dimension!')
    else:
        print('That is not a whole lot of cats')
except ValueError:
    print (' YOu did not enter a number')
