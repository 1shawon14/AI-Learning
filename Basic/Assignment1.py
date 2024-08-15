
'''User = input("Write anything:")
print(f'Your input is: {User}')'''
#Find is the number is positive of negative
''' 
num = int(input("enter a number: "))
if num > 0:
    print("The number is positive")
elif num <0:
    print("The number is negative")
else:
    Print("The number is Zero")
    '''
    
#Find the highest number
'''
num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))
num3 = int(input("Enter the third num: "))

if num1>num2 and num1>num3:
    print(f"The highest number is {str(num1)}")
elif num2>num1 and num2>num3:
    print(f"The highest number is {str(num2)}")
else:
    print(f"The highest number is {str(num3)}")
    '''
    
#Write factorial of a number
'''
n = int(input("enter a number: "))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(f'Factorial of the number is {factorial(n)}')'''

#Swipe the value
'''
a = int(input("enter a number: "))
b = int(input("Enter another number: "))

print(f'Before swipe the value the numbers are a={a} and b={b}')
a,b = b,a
print(f"Now the numbers are a={b} and b={a}")
'''
#Write a Python program to convert Celsius to Fahrenheit.
'''
c = int(input("Write the celcius value: "))
f = (c *9/5)+32
print(f"The Ferhenhite value is {f}")
'''
#Write a Python program to check if a variable is of a specific data type.
'''
num = 23.25
if isinstance(num, float):
    print("Float")
else:
    print("Is not a float")
    '''

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print(f"Sorted list: {numbers}")