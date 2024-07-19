# wite a recursive function that determines whether a given
# string is palindrome (returning True) or not (returning False)

# a palindrome word is a word that reads the same from l-to-r and r-to-l
# example palindrome words: abba, deleveled, rotator, ...

from rtrace import trace


# decorator to print the stack trace of recurvive calls
@trace
def PalindromeRecursive(word):
  # your code goes here
  if len(word) in (0, 1):
    return True
  else:
    if word[0] == word[-1]:
      N = PalindromeRecursive(word[1:-1])
      return N and True
    else:
      return False
  pass


if __name__ == "__main__":
  print(PalindromeRecursive.trace("abba"))
  print(PalindromeRecursive.trace("deleveled"))
  print(PalindromeRecursive.trace("rotator"))
