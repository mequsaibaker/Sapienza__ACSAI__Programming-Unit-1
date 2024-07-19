# Write the following function that could be used as a sorting key:


# To order a list of strings ignoring the case, then in lexicographical order:
#
# ['bar', 'cat', 'Cat', 'car'] -> ['bar', 'car', 'Cat', 'cat']
def key_strings1(x):
  return x.lower()


l = ['bar', 'cat', 'Cat', 'car']
print(sorted(l, key=key_strings1))  # <- change this to sort with the new key


# To order a list of tuples of three integer positive elements considering
# the second element, then the first and finally the third
# [(1,5,6), (3,4,9), (1,1,1)] -> [(1,1,1), (3,4,9), (1,5,6)]
def key_tuples(x):
  return x[1], x[0], x[2]


l = [(1, 5, 6), (3, 4, 9), (1, 1, 1)]
print(sorted(l, key=key_tuples))  # <- change this to sort with the new key


# To order a list of strings considering the number of characters in increasing order,
# then the ending letter, then the lexicographical order:
#
# ['snake', 'caterpillar', 'rat', 'bat', 'dog'] -> ['dog', 'bat', 'rat', 'snake', 'caterpillar']
def key_strings(x):
  return len(x), x[-1], x


l = ['snake', 'caterpillar', 'rat', 'bat', 'dog']
print(sorted(l, key=key_strings))  # <- change this to sort with the new key


#To order a list of strings considering the number of vowels in decreasing order,
# then the whole length in increasing order, then the reverse alphabetical order.
# example:
#['pear', 'peach', 'apple', 'banana', 'avocado'] ->
#['avocado', 'banana', 'pear', 'peach', 'apple']
def key_vowels(x):
  return -(x.count('a') + x.count('e') + x.count('i') + x.count('o') +
           x.count('u')), len(x), sorted(x, reverse=True)


l = ['pear', 'peach', 'apple', 'banana', 'avocado']
print(sorted(l, key=key_vowels))  # <- change this to sort with the new key


# To order a list of positive integers so that the odd numbers appear before the even numbers
# and the odd numbers are in increasing order, while the even numbers are in
# decreasing order.
# [1,5,2,6,7,4,5,3,8] -> [1,3,5,5,7,8,6,4,2]
def key_numbers(x):
  return -(x % 2), (-1 + 2 * (x % 2)) * x


l = [1, 5, 2, 6, 7, 4, 5, 3, 8]
print(sorted(l, key=key_numbers))  # <- change this to sort with the new key
