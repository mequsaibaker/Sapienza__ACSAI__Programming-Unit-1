# Write a function that gets two strings representing filenames input_file and output_file.
# The input_file contains several rows with numbers separated by whitespaces and tabs.
# The function must write in output_file the averages of the numbers found in every row,
# in the same order and return the maximum computed average.

# Example: if input_file has the following content:
# 1 5 7
# 3 1.4 12
#
# the function has to return the value 5.466666666666666
# and write the following lines in output_file:
# 4.333333333333333
# 5.466666666666666


def reader(input_file):
  file_ref = open(input_file, 'r', encoding='utf8')
  lines = file_ref.readlines()
  file_ref.close()
  return lines


def find_average(lines):
  num_list = []
  num_avg = 0
  num_avg_list = []
  for line in lines:
    num_sum = 0
    num_count = 0
    num_list = line.strip().split(' ')
    for value in num_list:
      if value != '':
        num_sum += float(value.strip())
        num_count += 1
    num_avg = num_sum / num_count
    num_avg_list.append(num_avg)
  return num_avg_list


def writer(num_avg_list, output_file):
  file_ref = open(output_file, 'w', encoding='utf8')
  for value in num_avg_list:
    print(value, file_ref)
  file_ref.close()
  return None

def averages_in_file(input_file, output_file):
  lines = reader(input_file)
  num_avg_list = find_average(lines)
  return num_avg_list


print(averages_in_file('test01.txt', '1'))
