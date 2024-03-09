print("You can choose a pb from 1, 5 , 9, 13, 17")
i = int(input("Choose the pb: "))
if i == 9:
    for x in range(10):
        for y in range(10):
            square = (x * 10 + y) ** 2
            last_digit = square % 10
            if last_digit == y:
                print("{}{} is a valid number.".format(x, y))

if i == 5:
    def value_at_index(k):
        i = 0
        while k >= (i + 1) * (i + 2) // 2:
            i += 1
        return i
    k = int(input("Enter the index 𝒌: "))
    result = value_at_index(k)
    print(f"The value at index {k} is: {result}")


if i == 1:
    def compute_control_digit(n):
        while n >= 10:
            n = sum(int(digit) for digit in str(n))
        return n

    user_input = input("Enter an integer: ")

    try:
        integer = int(user_input)
        control_digit = compute_control_digit(integer)
        print(f"The control digit of {integer} is {control_digit}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if i == 13:
    def form_number_from_odd_positions(n):
        n_str = str(n)
        odd_position_digits = [n_str[i] for i in range(len(n_str)) if i % 2 == 0]
        formed_number = int(''.join(odd_position_digits))
        return formed_number

    user_input = input("Enter a natural number: ")

    try:
        n = int(user_input)
        if n < 0:
            print("Please enter a natural number (non-negative integer).")
        else:
            result = form_number_from_odd_positions(n)
            print(f"Number formed from odd positions in {n} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid natural number.")

if i == 17:
    def sum_of_digits(number):
        return sum(int(digit) for digit in str(number))


    def is_special_number(n):
        for m in range(1, n + 1):
            if n == m + sum_of_digits(m):
                return True
        return False


    user_input = input("Enter a number to verify if it's special: ")

    try:
        n = int(user_input)
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            if is_special_number(n):
                print(f"{n} is a special number.")
            else:
                print(f"{n} is not a special number.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

