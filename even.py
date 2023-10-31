"""
calculating the sum of all even numbers 
- 1,100
"""
sum=0
for number in range (1,100):  
   if number%2==0:
    print("{} number is divisible by 2".format(number))
    sum=sum+1
    print("{}total number divisible by 2 are",sum) 

