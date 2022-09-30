#Activity 3

a=[[1,0,0],[0,1,0],[0,0,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]

for indrow in range (3):
    c.append ([])
    for indcol in range(3):
        c[indrow].append (0)
        for indaux in range (3):
            c[indrow][indol] += a[indrow][indaux] * b[indcol][indaux]

print(c)

##Activity 4
# Write a python function that takes a list of N tuples as
#input and returns the perimeter of the polygon.
#Remember that your code should work for any value of N

def perimeter(listing):
    leng=len(listing)
    perimeter=0;
    for i in range(0,leng-1):
        dist= (((listing[i][0]-listing[i+1][0])**2)+
               ((listing[i][1]-listing[i+1][1])**2))**0.5
    perimeter = perimeter +dist
    perimeter=perimeter + (((listing [0][0]-listing[leng-1][0])**2)+((listing[0][1]-listing[leng-1][1])**2))**0.5
    return perimeter

L=[(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(L))

##Activity 5
def symDiff(a,b):
    e=set()
    for i in a:
        if i not in b:
            e.add(i)
            for i in b:
                if i not in a:
                    e.add(i)
                    return e
                set1=(0,1,2,4,5)
                set2=(4,5,7,8,9)
                print(symmDiff(set1,set2))
                print(set1.symmetric_difference(set2))
                print(set2.symmetric_difference(set1))
                print(set1^set2)
                print(set2^set1)

##Activity 6
sample={("sohaib","ali"): "024655468445",("aib","li"): "024655468445"
        ("sib","ai"): "123456780987654",}
firstname=input("enter the first name")
lastname=input("enter the last name")
searchtuple=(firstname,lastname)
if searchtuple in sample:
    print(sample[searchtuple])
    else:
        print("name not found")

##----------Task 1
#Write a program that prompts the user to input an integer and then outputs the number with the digits 
#reversed. For example, if the input is 12345, the output should be 54321.

Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse) 

##------------Task 2
# Write a program that reads a set of integers, and then prints the sum
#of the even and odd integers.


integers = [10, 21, 4, 45, 66, 93]
for num in integers:
 
    if num % 2 == 0:
        print(num, end=" ")

##------------Task 3
# Fibonacci series

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

##-------------Task 4
# python program for grading system

marks = float(input("Enter your marks i: "))

if marks >= 91:
    print("Grade: A")
elif marks >= 81 and marks <= 90:
    print("Grade:B ")
elif marks >= 71 and marks <= 80:
    print("Grade: C")
elif marks >= 61 and marks <= 70:
    print("Grade: D")
elif marks >= 50 and marks <= 60:
    print("Grade: E")
else:
    print("Grade: F")

##---------------Task 5
# factorial of that number.

num = int(input("Enter the number:  "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
