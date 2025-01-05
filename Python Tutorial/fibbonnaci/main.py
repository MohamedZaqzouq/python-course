def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    num = int(input("Enter the number of Fibonacci numbers to generate: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"Fibonacci sequence up to {num} numbers: {fibonacci(num)}")