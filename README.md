# WordHuntSolver
Components:
1. Anagrams.py
2. WordHunt.py
3. WordHuntStats.py
4. WordHunter.py
5. Image and Text Files

# 1. Anagrams.py

<img src="https://github.com/KriChau95/WordHuntSolver/assets/140979138/168fefc0-a17d-4493-9efd-89a3578aee98" width="252" alt="Anagram_iPhone">
<img src="https://github.com/KriChau95/WordHuntSolver/assets/140979138/7f7a9e12-8ac7-4c69-8ea1-3c257f35afbc" width="700" alt="Anagram_Words">

This is a Python program that helps play the GamePigeon game Anagrams. It takes in the 6 letters on the board provided as input and returns all possible words that can be formed using those 6 letters

# 2. WordHunt.py

<img src="https://github.com/KriChau95/WordHuntSolver/assets/140979138/e6a9d08e-a0fd-4d40-b90d-16be4b81bcb7" width="352" alt="Word_Hunt_iPhone">
<img src="https://github.com/KriChau95/WordHuntSolver/assets/140979138/49f6ec46-2bbe-4c72-8aeb-e5a01c3a3245" width="600" alt="Word_Hunt_Words">
<img src ="https://github.com/KriChau95/WordHuntSolver/assets/140979138/23e3d896-49d2-48e7-bf2c-19c70323ec21" width = "960 alt = "Word_Hunt_Boards">

This is a Python program that helps play the GamePigeon game Word Hunt. It takes in the 16 letters that form the 4x4 board as input in the terminal, and it:
1. displays in the terminal a list of all the words that can be found on that board. Along with a each word, it provides coordinate (a,b) that represents the starting square of the word and a series of directions that indicate where to swipe to reach each subsequent letter in the word
2. ceates a new pygame window that displays the Top 50 longest, highest-scoring words on the board in a visual format

# 3. WordHuntStats.py

<img src="https://github.com/KriChau95/WordHuntSolver/assets/140979138/0a3558b7-f52a-43f2-a6fd-4c02b02857e2" width="1000" alt="Word_Hunt_Stats">

This python program uses matplotlib to plot some interesting statistics and patterns across all the possible Word Hunt words. For example:
* the frequency of every letter across that set of possible words
* the frequency of substrings of lengths 2-8 across that set of possible words
* the weighted scores of the letters and substrings depending on the size of the words they appear in

# 4. WordHunter.py

<img src="https://github.com/KriChau95/WordHuntSolver/assets/140979138/263553db-91f3-49b0-8597-09402e4f62c9" width="1000" alt="Word_Hunt_Stats">

This python program uses:
* OpenCV image capturing and processing in conjunction with
* pytesseract text recognition
and prompts the user to take a picture of their Word Hunt board. Open camera window, and then press the "s" key to capture the image of the board.
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
