# WordHuntSolver
This program has a few components:
1. Anagrams.py
2. WordHunt.py
3. WordHuntStats.py
4. WordHunter.py
5. Image and Text Files

# 1. Anagrams.py
This is a Python program that helps play the GamePigeon game Anagrams. It takes in the 6 letters on the board provided as input and returns all possible words that can be formed using those 6 letters

# 2. WordHunt.py
This is a Python program that helps play the GamePigeon game Word Hunt. It takes in the 16 letters that form the 4x4 board as input in the terminal, and it:
1. displays in the terminal a list of all the words that can be found on that board. Along with a each word, it provides coordinate (a,b) that represents the starting square of the word and a series of directions that indicate where to swipe to reach each subsequent letter in the word
2. ceates a new pygame window that displays the Top 50 longest, highest-scoring words on the board in a visual format

# 3. WordHuntStats.py
This python program uses matplotlib to plot some interesting statistics and patterns across all the possible Word Hunt words. For example:
* the frequency of every letter across that set of possible words
* the frequency of substrings of lengths 2-8 across that set of possible words
* the weighted scores of the letters and substrings depending on the size of the words they appear in

# 4. WordHunter.py
This python program uses:
* OpenCV image capturing and processing in conjunction with
* pytesseract text recognition
and prompts the user to take a picture of their Word Hunt board
It then carries out the functions described in **2. Word Hunt.py**

# 5. Image and Text Files
**Transformations** is a folder used by WordHunter.py to store the intermediate image transformations performed by OpenCV
**Dictionary.txt** is the reference dictionary that contains all the English words considered by the programs
**ShavedDict.txt** is a modified dictionary that only contains words of 6 letters in length or shorter - used for **1. Anagrams.py**

# Installations Required
Modules which need to be downloaded and imported, along with the appropriate installation commands

* **PyGame**:  ```pip install pygame``` - Needed for 2,4
* **MatPlotLib**:  ```pip install matplotlib``` - Needed for 3,4
* **OpenCV**: ```pip install opencv-python``` - Needed for 4
* **PyTesseract**:  ```pip install pytesseract``` - Needed for 4
* **Pillow** : ```pip install Pillow``` - Needed for 4
* **NumPy**: ```pip install numpy``` - Needed for 4
