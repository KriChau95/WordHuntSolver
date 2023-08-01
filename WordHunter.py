import cv2
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image, ImageEnhance
import numpy as np
import pygame as p

# Set path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    # Read the current frame from the camera
    _, frame = camera.read()
    
    # Display the frame
    cv2.imshow('Camera', frame)
    
    # Click on the 's' key to capture an image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the captured image
        cv2.imwrite('captured_image.jpg', frame)
        
        # Release the camera and close the OpenCV windows
        camera.release()
        cv2.destroyAllWindows()
        break

def display(im_path):
    dpi = 80
    im_data= plt.imread(im_path)
    height, width = im_data.shape # look into ", depth"

    # what size does the figure need to be in inches to fit the image
    figsize = width/float(dpi), height / float(dpi)

    # create a figure of the right size with one axis that takes up the full figure
    fig = plt.figure(figsize = figsize)
    ax = fig.add_axes([0,0,1,1])

    # hide spines, ticks, etc
    ax.axis("off")

    # display the image
    ax.imshow(im_data, cmap = "gray")

    plt.show()   

# 00 - Saving the Image File
image_file = "captured_image.jpg"
img = cv2.imread(image_file)

# 01 - Inverting the Image

inverted_image = cv2.bitwise_not(img)
cv2.imwrite("Transformations/inverted.jpg", inverted_image) 

# 02 - Grayscale

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv2.imwrite("Transformations/gray.jpg", gray_image)

# 03 - Black and White

thresh, im_bw = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("Transformations/bw.jpg", im_bw)

# 04 - Noise Removal

def noise_removal(image):
    kernel = np.ones((1,1), np.uint8)
    image = cv2.dilate(image, kernel, iterations = 1)
    kernel = np.ones((1,1), np.uint8)
    image = cv2.erode(image, kernel, iterations = 1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)

no_noise = noise_removal(im_bw)
cv2.imwrite("Transformations/no_noise.jpg", no_noise)

# 05 - Flood Fill

mask = np.zeros((no_noise.shape[0]+2, no_noise.shape[1]+2), np.uint8)
seed_point = (50,50)
new_color = (255, 255, 255)
retval, filled_image, mask, rect = cv2.floodFill(no_noise, mask, seed_point, new_color)

cv2.imwrite("Transformations/flood.jpg", filled_image)

# 06 - Dilation and Erosion Functions - techniques not used in this specific case

def thin_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernel, iterations = 1)
    image = cv2.bitwise_not(image)
    return (image)

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations = 1)
    image = cv2.bitwise_not(image)
    return (image)

# display("Transformations/flood.jpg")

# perform text recognition using pytesseract; whitelist all letters in the alphabet and space character
text = pytesseract.image_to_string(filled_image, config = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

# Word Hunting - see WordHunt.py for detailed comments for this section

def print_board(board):
    print("BOARD:\n")
    for i in range(16):
        if i % 4 == 3:
           print(board[i])
        else:
           print(board[i], end = " ")
 
board_input = ""
for i in range(len(text)):
    if text[i].isalpha():
        board_input += (text[i])

if len(board_input) != 16:
   print(text)
   exit(0)

board_letters = list(board_input)

print_board(board_input)

f = open("Dictionary.txt", "r")
lines = f.readlines()

word_list = []
for i in range(0, len(lines)):
  word_list.append(lines[i][:-1])

word_list[-1] = "ZZZS"

def is_possible (word):
  temp = board_letters.copy()
  word_letters = list(word)
  for letter in word_letters:
    try:
      temp.remove(letter)
    except:
      return False
  return True

possible_list = []

for j in range(0, len(word_list)):
  if is_possible(word_list[j]) and len(word_list[j]) >=3 and len(word_list[j]) <=16:
    possible_list.append(word_list[j])

class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False

root = TrieNode()

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

for i in range(4):
  for j in range(4):
    recurse(i, j, "", "(" + str(i) + ", " + str(j) + ")", visited, root)

solutions_list.sort(key = lambda y: len(y[1]))

existing = set()
no_dup_sols = [(a,b) for a,b in solutions_list if not(a in existing or existing.add(a))]

for item in no_dup_sols:
  print(item)

max_score = 0

score = {
  3: 100,
  4: 400,
  5: 800,
  6: 1400,
  7: 1800,
  8: 2200,
  9: 2600,
}

for item in no_dup_sols:
  if (len(item) > 9):
    continue
  max_score += score[len(item[0])]

print(max_score)

# A function to draw a board with inputs of the board letters, starting position, and a specific word found in the board - solution
def draw_board(board_input, start_x, start_y, cell_size, solution):
  font = p.font.SysFont("CourierNew", 35, False, False)

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
  font = p.font.SysFont("Georgia", 22, False, False)
  text_object = font.render(word, 0, p.Color("Red"))
  text_location = p.Rect(start_x + 20, start_y + 160, 10, 50)
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
          draw_board(board_input, 100 + (i - 1) * 175, 25 + (j - 1) * 200, 40, no_dup_sols[index])

    p.display.flip()
    clock.tick(60)

p.quit()