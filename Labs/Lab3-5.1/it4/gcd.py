def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_gcd_between_indices(my_list, from_index, to_index):
    if from_index < 0 or to_index >= len(my_list) or from_index > to_index:
        return None  # Invalid index range

    numbers = my_list[from_index:to_index + 1]
    if not numbers:
        return None  # Empty range

    # Calculate the GCD of the numbers in the specified range
    result_gcd = numbers[0]
    for number in numbers[1:]:
        result_gcd = get_gcd(result_gcd, number)

    return result_gcd