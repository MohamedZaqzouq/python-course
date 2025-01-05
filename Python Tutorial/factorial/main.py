number=input("enter number you want to calculate its factorial: ")
number=int(number)
factorial=1
while number>0:
    factorial=factorial*number
    number=number-1
print("Factorial of the number is: ",factorial)
