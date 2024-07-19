# Write a function that gets a dictionary of the type {key:integer list}
# and returns a new dictionary with the same keys and with values the
# average of the integers in the original dictionary list.

# Example: average_dict({5:[3,6,9], 0:[5,5,5], 'a':[4,4,5,5]}) -> {5:6.0, 0:5.0, 'a':4.5}


def average_dict(num_dict):
  dict_avg = {key: key for key in num_dict.keys()}
  for key in dict_avg.keys():
    dict_avg[key] = sum(num_dict[key]) / len(num_dict[key])
  return dict_avg


a_dict = {5: [3, 6, 9], 0: [5, 5, 5], 'a': [4, 4, 5, 5]}
print(average_dict(a_dict))
