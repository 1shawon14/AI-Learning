'''
n = int(input('Enter a number: '))
if n>0:
    if n%2==0:
        print('The number is positive and even')
    elif n%2 != 0:
        print('The number is positive and odd')
    else:
        print("The number is Zero")
else:
    print("The number is negative")
    '''
'''
for i in range (1,50):
    print(i)
    '''
'''
i=1
while i<=20:
    print(i)
    i+=1
    '''
'''
for i in range(5):
    for j in range(5):
        print("*",end=' ')
    print()
'''
'''
tot = 0
while True:
    num = float(input())
    if num ==0:
        break
    tot += num
print(tot)'''
'''
for i in range(1, 11):
    if i == 5:
        continue
    print(i)'''
'''  
factorial = 1
i = 1
number = int(input())
while i<=number:
    factorial*=i
    i+=1
print(factorial)
'''
'''
num = int(input())
while num>0:
    digit= (num%10)
    main = (num//10)
    ans =  digit + main
    print(ans)
    break'''
    
n = int(input("Enter the number of Fibonacci numbers to print: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1