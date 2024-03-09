def is_prime(a):
    if a == 0: # 0 is not a prime number
        return False
    else:
        if a <= 3: # 2 and 3 are prime numbers
            return True
        for index in range(2, (a // 2) + 1):
            if a % index == 0:
                return False
    return True
# function who verifies if a number is prime or not

def get_primes_between_indices(my_list, from_index, to_index):
    prime_list = [] # empty list
    for index in range(from_index, to_index):
        if is_prime(my_list[index]):
            prime_list.append(my_list[index])
    return prime_list