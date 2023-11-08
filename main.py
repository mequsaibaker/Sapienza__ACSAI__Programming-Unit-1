# look and read off the digits

# write a function LookAndSay(n, k) that, starting from
# the provided positive integer n, returns a list
# of numbers, in which each number is obtained
# by looking and saying the previous one, k times

# note: the numbers are returned as strings

# for example, given n=1 and k=8, the numbers are:

# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221

# and the function returns ["1", "11", "21", "1211", "111221",
# "312211", "13112221", "1113213211", "31131211131221"]


def LookAndSay(n, k):
  # your code goes here
  num_list = []
  num_str = str(n)
  for iteration in range(k):
    num_str_len = len(num_str)
    num_str = ''
    ind = 0
    while ind < num_str_len:
      current_char = num_str[ind]
      num_count = 1
      while num_str[ind + num_count] == current_char:
        num_count += 1
      num_str += current_char * num_count
    num_list.append(num_str)
  pass


if __name__ == "__main__":
  print(LookAndSay(1, 8))
