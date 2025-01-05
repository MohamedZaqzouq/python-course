def fibonaci(n):
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
def main():
    n=int(input("Enter the number of Fibonacci numbers to generate: "))
    print(f"Fibonacci sequence up to {n} numbers: {fibonaci(n)}")
main()