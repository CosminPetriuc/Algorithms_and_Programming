def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        if not is_prime(my_list[i]):
            my_list.pop(i)