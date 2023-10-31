'''
A python script to use multiple if
'''
Marks=int(input("Enter student marks: "))
if Marks>=0 and Marks<=30:
    print("{}E".format(Marks))
elif Marks>=31 and Marks<=40:
    print("{} D+".format(Marks))
elif Marks>=41 and Marks<=49:
    print("{} C-".format(Marks))
elif Marks>=50 and Marks<=59:
    print("{} C+".format(Marks)) 
elif Marks>=60 and Marks<=69:
    print("{} B-".format(Marks))
elif Marks>=70 and Marks<=79:
    print("{} B+".format(Marks)) 
elif Marks>=80 and Marks<=89:
    print("{} A".format(Marks))                  