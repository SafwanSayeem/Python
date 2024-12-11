import sys

def get_number(count):
    numbers = []
    for i in range(count):
        number = input(f"Number {i + 1}: ")
        try:
            number = float(eval(number))  
            numbers.append(number)
        except (ValueError, SyntaxError):
            print("Please enter valid mathematical expressions.")
            return None
    return numbers

def get_BIGnumber(count):
    Big_numbers = []
    for i in range(count):
        Big_number = input(f"Big Number {i + 1}: ")
        try:
            evaluated_value = float(eval(Big_number))
            Big_numbers.append((Big_number, evaluated_value))  
        except (ValueError, SyntaxError):
            print("Please enter a valid expression.")
            return None
    return Big_numbers

def Big_basic_operation(Big_numbers):
    print("Available operations: Greatest number, Lowest number, Unit digit")
    Big_operation = input("What would you like to do: ").strip().lower()

    if Big_operation == "greatest number":
        max_value_tuple = max(Big_numbers, key=lambda x: x[1])  
        print(f"The greatest number is {max_value_tuple[0]}.")
    elif Big_operation == "lowest number":
        min_value_tuple = min(Big_numbers, key=lambda x: x[1])  
        print(f"The lowest number is {min_value_tuple[0]}.")
    elif Big_operation == "unit digit":
        unit_digits = [int(str(int(value[1]))[-1]) for value in Big_numbers]
        print(f"The unit digits are: {unit_digits}")
    else:
        print("Invalid operation.")

def basic_operations(numbers, count):
    print("Available operations: addition, subtraction, multiplication, division, or next for advanced options.")
    print("Type 'BIG' for operations on big numbers (e.g., 4**10, 10**6, etc.).")
    operation = input("What would you like to do: ").strip().lower()

    if operation == "big":
        Big_numbers = get_BIGnumber(count)
        if Big_numbers:
            Big_basic_operation(Big_numbers)

    elif operation == "next":
        print("Advanced operations: greatest of the numbers, lowest of the numbers, average")
        advanced_operation = input("What would you like to do: ").strip().lower()

        if advanced_operation == "greatest of the numbers":
            print(f"The greatest number is {max(numbers)}")
        elif advanced_operation == "lowest of the numbers":
            print(f"The lowest number is {min(numbers)}")
        elif advanced_operation == "average":
            print(f"The average is {sum(numbers) / count}")
        else:
            print("Invalid operation.")

    elif operation == "addition":
        print(f"The sum is {sum(numbers)}")
    elif operation == "subtraction":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print(f"The result of subtraction is {result}")
    elif operation == "multiplication":
        result = 1
        for num in numbers:
            result *= num
        print(f"The product is {result}")
    elif operation == "division":
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Error: Division by zero is not allowed.")
                return
            result /= num
        print(f"The result of division is {result}")
    else:
        print("Invalid operation.")

print("Welcome to my calculator (2nd edition)")
try:
    Numcount = int(input("How many numbers are you using: "))
    if Numcount <= 0:
        print("Please enter a positive number.")
        sys.exit()
    numbers = get_number(Numcount)
    if numbers:
        basic_operations(numbers, Numcount)
except ValueError:
    print("Invalid input. Please enter a valid number.")
