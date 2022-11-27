array = [42, 24, 17, 69, 33, 5, 4, 61, 52, 12, 54]


def prime_check(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


array = filter(prime_check, array)

print(*array)
