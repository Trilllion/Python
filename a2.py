print ('')                                                                      #AESTHETICS
print ('This program will not close until you enter a valid integer.\n')        #AESTHETICS
print ('It will repeat for about 70 times before automatically exiting.\n')     #AESTHETICS
print ('Now please enter an integer\n')
def collatz(number):                                                            #Function
    if number % 2 == 0:
        a = number // 2
        return (a)
    elif number % 2 == 1:
        k = 3*number + 1
        return(k)
for x in range(70,1, -1):                                                       #To repeat input till user gets it right.
    try:                                                                        #To resolve ValueError

            number = int(input())
            if number <= 1:
                print ('Please enter an integer larger than 1.\n')
            elif number > 1:
                break
    except ValueError:
         print('Please enter a valid integer.\n')
print(collatz(number))                                                          #Instead of printing in the function,
                                                                                #We print at the end.
