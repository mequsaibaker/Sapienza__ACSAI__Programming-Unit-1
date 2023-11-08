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
  return matrix


def TransposeMatrixFromFile(source_file_path, destination_file_path):
  # your code goes here
  pass


if __name__ == "__main__":
  TransposeMatrixFromFile("original_matrix.txt", "transposed_file_path")
