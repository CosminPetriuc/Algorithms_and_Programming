#1 Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compute the sum
sum_result = num1 + num2

# Display the result
print("The sum of {} and {} is: {}".format(num1, num2, sum_result))

#2 Input the value of n
n = int(input("Enter a positive integer n: "))

# Initialize the product to 1
product = 1

# Calculate the product of the first n natural numbers
for i in range(1, n + 1):
    product *= i

# Display the result
print("The product of the first {} natural numbers is: {}".format(n, product))

#3
def is_perfect_number(num):
    if num <= 0:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum == num


# Input a number
num = int(input("Enter a positive integer: "))

# Check if it's a perfect number
if is_perfect_number(num):
    print("{} is a perfect number.".format(num))
else:
    print("{} is not a perfect number.".format(num))
