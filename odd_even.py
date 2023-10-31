''''
a python program to determine if the number is odd or even
'''
count=0
for number in range(1,100):
    '''
    arithmetic operators
    addituion +
    substraction -
    division /
    musltiplication *
    modulation %
    '''
    if number%7==0:
        print("{} is divisible by 7 ".format(number))
        count=count+1
    else:
        print("{} is not divisible by 7".format(number))

    print("Total numbers divisible by 7 are",count)