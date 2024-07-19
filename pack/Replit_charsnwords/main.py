#Write a function that gets a list of strings and returns a
# dictionary with keys to all the characters found in the
# strings of the list and, as values, a list of all the strings
# that contain the character of the key. The lists in the
# dictionary are sorted in alphabetical order.

# Example: chars_n_words(['dog', 'hot', 'dot']) -> {'d':['dog', 'dot'], 'o':['dog', 'dot', 'hot'], 'g':['dog'], 'h':['hot'], 't':['dot', 'hot']}


def chars_n_words(str_list):
  char_set = set(''.join(str_list))
  char_dict = {}
  sorted_str_list = sorted(str_list)
  for char in char_set:
    char_word_list = []
    for word in sorted_str_list:
      if char in word:
        char_word_list.append(word)
    char_dict[char] = char_word_list
  return char_dict


print(chars_n_words(['dog', 'hot', 'dot']))
