# Store dictionary to lines
f = open("Dictionary.txt", "r")
lines = f.readlines()

# Filter the impossible words (7 letters or more) out of the dictionary
fileNew = open('ShavedDict.txt', 'w')

n = 279496
# Store all possible words to word_list
word_list = []

for i in range(0,n):
    word_list.append(lines[i][:-1])

word_list[-1] = 'ZZZS'

# 6 inputted letters on board
anagram = input("Enter the six letters:").upper()

for word in word_list:
    if (len(word) >=3 and len(word) <=6):
        fileNew.write(word + "\n")

# boolean function that determines whether a word in the dictionary is possible to form using the 6 letters on the board
def isPossible (word):
  temp = list(anagram).copy()
  word_letters = list(word)
  for letter in word_letters:
    try:
      temp.remove(letter)
    except:
      return False
  return True

possible_list = []

for word in word_list:
    if(len(word) >=3 and len(word) <=6): # the range of accepted word lengths is 3-6
        if(isPossible(word)):
            possible_list.append(word)

# sort list of possible words by length
possible_list.sort(key = len)
print(possible_list)

# score calculating algorithm based on length of found words
def get_score(possible_list):
    score = 0
    for item in possible_list:
        if len(item) == 6:
            score += 2000
        if len(item) == 5:
            score += 1200
        if len(item) == 4:
            score += 400
        if len(item) == 3:
            score += 100
    return score

# display all possible words
print(get_score(possible_list))
            
