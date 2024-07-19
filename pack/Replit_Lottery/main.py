'''A lottery works as follows.
Each participant pays in €5 and chooses six numbers in the range [1, 90].
The total amount of collected money is shared among the winners.
To determine the winner(s), 1 number in the same range is drawn at random;
all lottery participants who chose that number share equally the winning.
Write a function lottery_winners(participants, x) that takes a dictionary
(containing the participants names and played numbers) and the value
of the randomly drawn number x and returns a tuple with the list of the names
of the winners (in alphabetical order) and the amount won by each
(as a flot, rounded at the first decimal digit).
For example, if the participants are:
{"Donald" : [23, 21, 20, 34, 15, 23], "Boris" : [17, 16, 3, 7,26, 42],
"Theresa" : [13, 90, 47, 17, 1, 11] }
and the draw number is 17
your function should return (["Boris", "Theresa"], 7.5)
'''

def lottery_winners(participants, x):
  winners = []
  for key, value in participants.items():
    if x in value:
      winners.append(key)
  return sorted(winners), 5 * len(participants) / len(winners)

if __name__ == "__main__":
  print(lottery_winners({ "Donald" : [23, 21, 20, 34, 15, 23], "Boris" : [17, 16, 3, 7, 26, 42], "Theresa" : [13, 90, 47, 17, 1, 11] }, 17))


