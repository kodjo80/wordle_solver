## program which checks all *.txt files in working directory and parse all words in them.
## If the words are of lnght of 5, then the words are stored in a file for further manipulations.

import glob
import os

# os.chdir(r'directory where the files are located')
myFiles = glob.glob('*.txt')
print(myFiles)

word_list_unique = set()

for file in myFiles:
    contents = list()
    with open(file, 'r') as f:
        contents = f.read().splitlines()
    print(file)
    word_list_unique.update(contents)
    # print(contents)

print(f"All unique words are: {len(word_list_unique)}")
word_list_5 = [word for word in word_list_unique if len(word) == 5]
word_list_unique = list(word_list_unique)

print(f"All unique words with length of 5 are: {len(word_list_5)}")
with open('5_list.txt', 'w') as f:
    for word in word_list_5:
        f.write("%s\n" % word)

print("All words with lenght of 5 are saved in file '5_list.txt'")

print(word_list_5)

