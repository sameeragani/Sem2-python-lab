"""#Temperature Conversion
print("Enter 'c' to covert from Celsius to Fahrenheit")
print("Enter 'f' to covert from Fahrenheit to Celsius")
choice=input("Enter your choice:")
if choice=='c':
    celsius=float(input("Enter temperature in Celsius:"))
    fahrenheit=(celsius*9/5)+32
    print('%.2f Celsius is:%0.2f Fahrenheit'%(celsius,fahrenheit))
elif choice=='f':
    fahrenheit=float(input("Enter temperature in Fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    print('%.2f Fahrenheit is:%0.2f Celsius' %(fahrenheit,celsius))
else:
    print('Invalid Input')



#Student Mark Processing
a=int(input("Enter the marks obtained in subject 1: "))
b=int(input("Enter the marks obtained in subject 2: "))
c=int(input("Enter the marks obtained in subject 3: "))
d=int(input("Enter the marks obtained in subject 4: "))
e=int(input("Enter the marks obtained in subject 5: "))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("Grade C")
elif per>=40:
    print("Grade D")
else:
    print("Grade E")"""


"""#area of rectangle triangle square circle
a=int(input())
b=int(input())
area_of_rectangle=a*b
print("Area of rectangle:",area_of_rectangle)
b=int(input())
h=int(input())
area_of_triangle=1/2*b*h
print("Area of triangle:",area_of_triangle)
r=int(input())
area_of_circle=3.14*r*r
print("Area of circle:",area_of_circle)
a=int(input())
area_of_square=a*a
print("Area of square:",area_of_square)

#fibonacci series
n=int(input("Enter the Number:"))
a,b=0,1
print(a, b, end=" ")
for i in range(2,n):
    a,b=b,a+b
    print(b,end=" ")"""

"""#factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input('enter the number:'))
print(f"The factorial is {factorial(num)}")"""

#create a list of array from that count how many odd and even numbers are there
def count_odd_even(numbers):
    odd_count = 0
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
odd_count, even_count = count_odd_even(numbers)
print(f"The list of numbers is: {numbers}")
print(f"Number of odd numbers: {odd_count}")
print(f"Number of even numbers: {even_count}")




