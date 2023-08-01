f = open("Dictionary.txt", "r")
lines = f.readlines()

fileNew = open('ShavedDict.txt', 'w')

n = 279496
word_list = []

for i in range(0,n):
    word_list.append(lines[i][:-1])

word_list[-1] = 'ZZZS'

anagram = input("Enter the six letters:").upper()

for word in word_list:
    if (len(word) >=3 and len(word) <=6):
        fileNew.write(word + "\n")

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
    if(len(word) >=3 and len(word) <=6):
        if(isPossible(word)):
            possible_list.append(word)

possible_list.sort(key = len)
print(possible_list)

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

print(get_score(possible_list))
            
