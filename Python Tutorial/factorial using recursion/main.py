def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
def main():
    number=input("enter number you want to calculate its factorial: ")
    number=int(number)
    print("Factorial of the number is: ",factorial(number))
main()