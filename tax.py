"""
Aprogram that computes tax based on salary.
if salary is more than 30,000 tax is 1.5%.
otherwise tax is 0%
"""
salary=int(input("Enter salary :"))
if salary>=30000:
    tax=1.5/100*salary
else:
    tax=0/100*salary
print("tax base on salary {}".format(tax))   