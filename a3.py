def collatz(number):                                                            #Function
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print (number)

        elif number % 2 == 1:
            number = 3*number + 1
            print (number)
                                                                                
try:                                                                            #To resolve ValueError
    number = int(input())
    if number <= 1:
        print ('Please enter an integer larger than 1.\n')

except ValueError:
    print('Please enter a valid integer.\n')

collatz(number)
