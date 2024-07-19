# Write a function that gets a list of integers and returns
# a dictionary in which the keys are the prime numbers of the
# lists and the values are the largest multiples of the key
# in the list.
#
# Example: [5, 33, 6, 2, 30, 1, 3] -> {5:30, 2:30, 1:33, 3:33}


def is_prime(x):
  if x % 2 == 0:
    return True
  for i in range(3, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True


def primes_with_multiples(num_list):
  dict_prime = {key: 0 for key in num_list if is_prime(key)}
  for key, value in dict_prime.items():
    for num in num_list:
      if not is_prime(num) and num % key == 0 and num > dict_prime[key]:
        dict_prime[key] = num
  return dict_prime



int_list = [5, 33, 6, 2, 30, 1, 3]
print(primes_with_multiples(int_list))
