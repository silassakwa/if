'''
A pthon script that compute commision based on sales
-the user input his/her sales
-the program computes the commision based on sales
sales above 50000 commision is 2.5%
sales below 50000 commsion is 1.5%
'''
Sales=int(input("Enter sales: "))
if Sales >=500000:
    commission=Sales*2.5/100
else:
    commission=Sales*1.5/100
print("Your Sales is {} ".format(Sales))
print("Your commsion is {} ".format(commission))