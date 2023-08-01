import matplotlib.pyplot as plt

# Reading in all the letters from a Dictionary text file
f = open("Dictionary.txt", "r")
lines = f.readlines()

# Saving each item in the dictionary to a list of words - word_list
word_list = []
for i in range(0, len(lines)):
  word_list.append(lines[i][:-1])

word_list[-1] = "ZZZS"

# this list will store all the words from the dictionary that could possibly be a Word Hunt word
possible_list = []

for j in range(0, len(word_list)):
  if len(word_list[j]) >=3 and len(word_list[j]) <=9: # the acceptable size of a word in Word Hunt is between 3 and 9 letters
    possible_list.append(word_list[j])

letter_frequency = dict()
for word in possible_list:
  for letter in word:
    if letter in letter_frequency:
      letter_frequency[letter] += 1
    else:
      letter_frequency[letter] = 1
    
# Score of words based on their lengths, each pair is (length_of_word, score)
score = {
  3: 100,
  4: 400,
  5: 800,
  6: 1400,
  7: 1800,
  8: 2200,
  9: 2600,
}

# Determining the weighted letter score of all letters by multiplying the frequency of each letter by the corresponding score of each word it occurs in
weighted_letter_score = dict()

for word in possible_list:
  for letter in word:
    if letter in weighted_letter_score:
      weighted_letter_score[letter] += score[len(word)]
    else:
      weighted_letter_score[letter] = score[len(word)]

# Plotting frequency of letters in Word Hunt accepted words (alphabetical order)

fig, ax = plt.subplots()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_list = list()
for letter in alphabet:
  alphabet_list.append(letter)

letters = alphabet_list

counts = list()
for letter in alphabet_list:
  counts.append(letter_frequency[letter])

bar_labels = alphabet_list

bar_colors = ["tab:blue"] * 26

ax.bar(letters, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Frequency')
ax.set_title('Frequency of Letters in Word Hunt Accepted Words')

# Plotting weighted score of letters in Word Hunt accepted words (alphabetical order)

fig, ax = plt.subplots()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_list = list()
for letter in alphabet:
  alphabet_list.append(letter)

letters = alphabet_list

weights = list()
for letter in alphabet_list:
  weights.append(weighted_letter_score[letter])

bar_labels = alphabet_list

bar_colors = list()
for i in range(26):
  bar_colors.append("tab:blue")

ax.bar(letters, weights, label=bar_labels, color=bar_colors)

ax.set_ylabel('Frequency')
ax.set_title('Weighted Score of Letters in Word Hunt Accepted Words')

# Generalized function for plotting:
# x - size of substring
# n - top n most frequent substrings
def plot_substring_frequency(x, n):
  x_frequency = dict()
  for word in possible_list:
    if len(word) >= x:
      for i in range(len(word)-(x-1)):
        if word[i:i+x] in x_frequency:
          x_frequency[word[i:i+x]] += 1
        else:
          x_frequency[word[i:i+x]] = 1

  sorted_dict = dict(sorted(x_frequency.items(), key=lambda item: item[1], reverse=True))

  fig, ax = plt.subplots()

  top_n_substrings = list(sorted_dict.keys())[:n]
  top_n_counts = list(sorted_dict.values())[:n]

  substrings = top_n_substrings
  counts = top_n_counts

  bar_labels = top_n_substrings

  bar_colors = ["tab:blue"] * len(top_n_substrings)

  ax.bar(substrings, counts, label = bar_labels, color = bar_colors)
  ax.set_ylabel("Frequency")
  ax.set_title("Frequency of " + str(x)+ "-letter substrings in Word Hunt Acceptable words - Sorted")

# Generalized function for plotting:
# x - size of substring
# n - top n most frequent substrings
def plot_substring_weighted_scores(x, n):
  weighted_substring_score = dict()
  for word in possible_list:
    if len(word) >= x:
      for i in range(len(word)-(x-1)):
        if word[i:i+x] in weighted_substring_score:
          weighted_substring_score[word[i:i+x]] += score[len(word)]
        else:
          weighted_substring_score[word[i:i+x]] = score[len(word)]

  sorted_dict = dict(sorted(weighted_substring_score.items(), key=lambda item: item[1], reverse=True))

  fig, ax = plt.subplots()

  top_n_substrings = list(sorted_dict.keys())[:n]
  top_n_weights = list(sorted_dict.values())[:n]

  substrings = top_n_substrings
  weights = top_n_weights

  bar_labels = top_n_substrings

  bar_colors = ["tab:blue"] * len(top_n_substrings)

  ax.bar(substrings, weights, label = bar_labels, color = bar_colors)
  ax.set_ylabel("Weighted Scores")
  ax.set_title("Weighted Scores of " + str(x)+ "-letter substrings in Word Hunt Acceptable words - Sorted")

# Plotting the frequency of various length substrings (the few highest occurring ones)

plot_substring_frequency(1, 26)
plot_substring_frequency(2, 25)
plot_substring_frequency(3, 25)
plot_substring_frequency(4, 25)
plot_substring_frequency(5, 20) # 20 most common 5-letter substrings
plot_substring_frequency(6, 15)
plot_substring_frequency(7, 15)
plot_substring_frequency(8, 10)

plot_substring_weighted_scores(1, 26)
plot_substring_weighted_scores(2, 25)
plot_substring_weighted_scores(3, 25)
plot_substring_weighted_scores(4, 25)
plot_substring_weighted_scores(5, 20) # Top 20 5-letter substrings with heaviest weight (proxy for assessing "value" on a board)
plot_substring_weighted_scores(6, 15)
plot_substring_weighted_scores(7, 15)
plot_substring_weighted_scores(8, 10)

print(len(possible_list))

plt.show()