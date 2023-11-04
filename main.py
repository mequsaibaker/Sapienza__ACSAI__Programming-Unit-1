# Write a function that gets a list of integers and returns
# a dictionary in which the keys are the prime numbers of the
# lists and the values are the largest multiples of the key
# in the list.
#
# Example: [5, 33, 6, 2, 30, 1, 3] -> {5:30, 2:30, 1:33, 3:33}

def is_primne(x):
    if x%2==0:
        return True
    for i in range(3, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def primes_with_multiples(int_list):
    pass

int_list = [5, 33, 6, 2, 30, 1, 3]
print(primes_with_multiples(int_list))
