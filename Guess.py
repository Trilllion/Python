import random
print('Hello, what might your name be?')
Name = input()
Number = random.randint (1,20)
print('Well ' + Name + ' I am thinking of a number between 1 and 20.')

for i in range (1,7):
    print ('Take a guess')
    NumberInput = int(input())
    if NumberInput > Number:
        print('Your guess is higher.')
    elif NumberInput < Number:
        print ('Your guess is lower.')
    elif NumberInput == Number:
        print ('You guess correctly, the number is ' + str(Number))
