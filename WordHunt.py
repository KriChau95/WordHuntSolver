import pygame as p

# board_input stores the board as a 16-letter string
board_input = input("Enter the board letters: ")
board_input = board_input.upper()

# board_letters stores the board as a list of 16 characters
board_letters = list(board_input)

for i in range (len(board_letters)):
  board_letters[i] = board_letters[i].upper()

# Reading in all the letters from a Dictionary text file
f = open("Dictionary.txt", "r")
lines = f.readlines()

# Saving each item in the dictionary to a list of words - word_list
word_list = []
for i in range(0, len(lines)):
  word_list.append(lines[i][:-1])

word_list[-1] = "ZZZS"

# This function takes in a word as input and determines if it is possible to form it from the set of characters on the 4x4 grid
# It does not take into account the position of the letters relative to each other on the board
# It is a screening to see if the word even has a fighting chance to be found on the board 
def is_possible (word):
  temp = board_letters.copy()
  word_letters = list(word)
  for letter in word_letters:
    try:
      temp.remove(letter)
    except:
      return False
  return True

# this list will store all the words from the dictionary that have a fighting chance of being a word after passing the filter described above
possible_list = []

for j in range(0, len(word_list)):
  if is_possible(word_list[j]) and len(word_list[j]) >=3 and len(word_list[j]) <=9: # the acceptable size of a word in Word Hunt is between 3 and 9 letters
    possible_list.append(word_list[j])

# The TrieNode class is used to create a Trie which is a condensed, cleaner way to store all possible words in the dictionary that have made it past the filter
class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False

root = TrieNode()

# This function uses depth first search in conjunction with the Trie that has all possible words to determine which words can be found on the
# specific 4x4 board given the positioning of the letters (adjacent letters of the word must appear in adjacent cells on the board)
def recurse(row, col, word, path, visited, node):

  if(row < 0 or row >=4 or col <0 or col >=4):
    return
  if(visited[row][col]):
    return

  letter = board[row][col]

  if letter not in node.children: 
    return

  word += letter
  visited[row][col] = True

  if(len(word) >=3 and node.children[letter].is_end_of_word):
    solutions_list.append((word, path))

  directions = [((1,0), ", D"), ((0,1), ", R"), ((-1,0), ", U"), ((0,-1), ", L"), ((1,-1), ", LD"), ((-1,1), ", RU"), ((1,1), ", RD"), ((-1,-1), ", LU")]

  for item in directions:
    x = item[0][0]
    y = item[0][1]
    d = item[1]
    if(row + x >= 0 and row + x <4 and col + y >=0 and col + y < 4):
      if(not visited[row + x][col + y]):
        recurse(row + x, col + y, word, path + d, visited, node.children[letter])

  visited[row][col] = False

# Making the Trie
for word in possible_list:
  curr_node = root
  for i in range(len(word)):
    letter = word[i]
    if letter not in curr_node.children:
      curr_node.children[letter] = TrieNode()
    curr_node = curr_node.children[letter]
    if(i == len(word) - 1):
      curr_node.is_end_of_word = True

board = list()
board.append(board_input[0:4])
board.append(board_input[4:8])
board.append(board_input[8:12])
board.append(board_input[12:16])

visited = [[False, False, False, False],[False, False, False, False], [False, False, False, False], [False, False, False, False]]

solutions_list = list()

# Printing out each word along with its starting square coordinate adn the corresponding directions to get to subsequent letters in the word
for i in range(4):
  for j in range(4):
    recurse(i, j, "", "(" + str(i) + ", " + str(j) + ")", visited, root)

# Sort the solutions by length
solutions_list.sort(key = lambda y: len(y[1]))

# Removing duplicate words from solution set
existing = set()
no_dup_sols = [(a,b) for a,b in solutions_list if not(a in existing or existing.add(a))]

for item in no_dup_sols:
  print(item)

max_score = 0

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

# Determine max possible score of board, asssumign all words are found
for item in no_dup_sols:
  if (len(item) > 9):
    continue
  max_score += score[len(item[0])]

print(max_score)

# A function to draw a board with inputs of the board letters, starting position, and a specific word found in the board - solution
def draw_board(board_input, start_x, start_y, cell_size, solution):
  font = p.font.SysFont("CourierNew", 25, False, False)

  # position_list contains the a list of the string positions of a specific solution; a list of numbers
  position_list = generate_color_letters(solution)
  start_index= position_list[0]

  for row in range(4):
      for col in range(4):
          index = row * 4 + col
          letter = board_input[index] if index < len(board_input) else ""
          if index == start_index:
            color = (255,0,0)
          elif index in position_list:
            position = position_list.index(index)
            color = (255 - 20 * position, 20 * position, 20 * position) # gradient effect
          else:
            color = (50, 50, 50) # color letters not a part of the word a dark gray
          text_object = font.render(letter, 0, p.Color(color))
          text_location = p.Rect(start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size)
          screen.blit(text_object, text_location)
  
  # Bold start letter
  text_object = font.render(board_input[start_index], 0, p.Color((255,0,0)))
  text_location = p.Rect(start_x + start_index % 4 * cell_size + 1, start_y + start_index//4 * cell_size + 1, cell_size, cell_size)
  screen.blit(text_object, text_location)

  # Draw word underneath
  word = solution[0]
  font = p.font.SysFont("Georgia", 15, False, False)
  text_object = font.render(word, 0, p.Color("Red"))
  text_location = p.Rect(start_x + 10, start_y + 125, 10, 50)
  screen.blit(text_object, text_location)

# Dictionary that has direction strings as keys and corresponding translations of indices in the board_letters string
letter_directions_to_str_translation = {
  "D" : 4,
  "R" : 1,
  "U" : -4,
  "L" : -1,
  "LD" : 3,
  "RU" : -3,
  "RD" : 5,
  "LU" : -5
}

# This function takes a specific word solution as input and returns the list of position indices in board_letters where it is found
def generate_color_letters(solution):
  path = solution[1]

  start_row = int(path[1])
  start_col = int(path[4])
  
  start_index_str = start_row * 4 + start_col
  
  directions_list = path[8:].replace(" ", "").split(",")
  
  board_str_index_list = [start_index_str]
  
  curr_index = start_index_str
  
  for direction in directions_list:
    board_str_index_list.append(curr_index + letter_directions_to_str_translation[direction])
    curr_index = curr_index + letter_directions_to_str_translation[direction]

  return board_str_index_list

p.init()
screen = p.display.set_mode((0,0), p.FULLSCREEN)
p.display.set_caption("Word Hunter")

clock = p.time.Clock()
screen.fill(p.Color("Black"))
running = True
while running:
  for event in p.event.get():
    if event.type == p.QUIT:
      running = False

    for j in range(5, 0, -1):
      for i in range(1, 11):
        index = -i - 10 * (j - 1)
        if (-index <=len(no_dup_sols)): # in case there are less than 50 total words found on the board
          draw_board(board_input, 10 + (i - 1) * 150, 10 + (j - 1) * 175, 30, no_dup_sols[index])

    p.display.flip()
    clock.tick(60)

p.quit()