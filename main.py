'''
write a function that reads a text file containing a sequence of words on multiple lines, separated by any number of spaces and returns the size of the longest word.
note that a word can be split on more than one line. for example, if you read in the content of the file in the following list (with readlines):

["abacus     bearing  colorf\n",
"ul    dedication entertain\n",
"ment  future  gamification"]

the function will return 13, as the longest word is "entertainment".
'''


def readTextInFile(filepath):
  file_ref = open(filepath, 'r', encoding='utf8')
  txt = file_ref.read()
  return txt


def removeNewLines(txt):
  return txt.replace("\n", "Hi")


def LongestWordInFile(filepath):
  # your code goes here
  txt = removeNewLines(readTextInFile(filepath))
  txt_len = len(txt)

  max_word_len = 0
  first_char_ind = 0
  last_char_ind = 0

  counter = 0
  while counter < txt_len:
    if first_char_ind.isalpha():
      first_char_ind = counter
      for ind in range(counter, txt_len):
        last_char_ind = counter + ind
        if not txt[last_char_ind].isalpha():
          counter += last_char_ind
          break
      max_word_len = max(max_word_len, last_char_ind - first_char_ind)
  pass


if __name__ == "__main__":
  txt = readTextInFile("testfile.txt")
  txt2 = txt.replace("\n", "Hi")
  print(txt2)
  print(LongestWordInFile("testfile.txt"))
