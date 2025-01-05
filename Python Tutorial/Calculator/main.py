first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
first_number = float(first_number)
second_number = float(second_number)
sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number if second_number != 0 else "Undefined (division by zero)"
print("Sum:", sum_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)