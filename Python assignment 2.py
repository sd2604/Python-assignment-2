#Check if a Number is Even or Odd

a=int(input("Enter a number"))
if a%2==0:
    print(a,"is an even number")
else:
    print(a,"is an odd number")

#Sum of Integers from 1 to 50 Using a Loop

total=0
for i in range(0,51):
    total=total+i

print('The sum of numbers from 1 to 50 is:',total)
