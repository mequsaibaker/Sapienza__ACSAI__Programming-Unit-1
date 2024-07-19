'''
write a function that takes a matrix (a list of lists) as input and returns the same matrix rotated by 90 degrees clockwise
below is an example with random numbers to demonstrate its usage.

input matrix:
[
    [8, 5, 2],
    [9, 6, 3],
    [7, 4, 1]
]

rotated matrix:
[
    [7, 9, 8],
    [4, 6, 5],
    [1, 3, 2]
]

'''


def RotateMatrix(matrix):
  # your code goes here
  rotated_m = []
  for r in range(len(matrix)):
    new_row = []
    for c in range(len(matrix[r]) - 1, -1, -1):
      new_row.append(matrix[c][r])
    rotated_m.append(new_row)
  return rotated_m


if __name__ == "__main__":
  input_matrix = [[8, 5, 2], [9, 6, 3], [7, 4, 1]]

  print(RotateMatrix(input_matrix))
