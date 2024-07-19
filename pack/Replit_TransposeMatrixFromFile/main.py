'''
create a function that performs the following actions:

    - load a rectangular matrix from a source text file
    - transpose the matrix (swap rows and columns)
    - save the transposed matrix to a destination text file

the function takes two parameters: the source file name (from which the original matrix is loaded) and the destination file name (where the transposed matrix will be saved).

suppose you have a source text file, 'original_matrix.txt', with the following content:

1 2
3 4
5 6

after running the function, the contents of 'transposed_matrix.txt' should be as follows:

1 3 5
2 4 6

note: the matrix can be stored in a list of lists; a list of lists is a list in which the items are lists; so, each item in the list is one row of the matrix, and each item in each sublist is one of the values of the matrix.
'''


def readMatrix(source_file_path):
  matrix = []
  file_ref = open(source_file_path, 'r', encoding="utf8")
  for line in file_ref:
    row = (line.strip()).split(' ')
    matrix.append(row)
  file_ref.close()
  return matrix


def transposeMatrix(matrix: list[list[str]]):
  transposed_m = []
  for row in range(len(matrix[0])):
    new_row = []
    for col in range(len(matrix)):
      new_row.append(matrix[col][row])
    transposed_m.append(new_row)
  return transposed_m


def writeMatrix(matrix: list[list[str]], destination_file_path):
  file_ref = open(destination_file_path, 'w', encoding="utf8")
  for row in range(len(matrix)):
    for ind, value in enumerate(matrix[row]):
      file_ref.write(value)
      if ind < len(matrix[row]) - 1:
        file_ref.write(' ')
    file_ref.write('\n')
  file_ref.close()
  return None


def TransposeMatrixFromFile(source_file_path, destination_file_path):
  # your code goes here
  matrix = readMatrix(source_file_path)
  transposed_m = transposeMatrix(matrix)
  writeMatrix(transposed_m, destination_file_path)
  return None


if __name__ == "__main__":
  print(readMatrix("original_matrix.txt"))
  print(transposeMatrix(readMatrix("original_matrix.txt")))
  TransposeMatrixFromFile("original_matrix.txt", "transposed_file_path")
