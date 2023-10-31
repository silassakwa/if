'''
A Python program to determine if the user is eligible to vote or not.
If age is above 18, the user can vote; otherwise, they cannot vote.
'''
Age = int(input("Enter your age: "))

if Age >= 18:
    print("Your age is {}; you are eligible to vote.".format(Age))
else:
    print("Your age is {} - you are not eligible to vote. Please try when you are 18 or older.".format(Age))






