from random import randint
from pprint import pprint


def open_file():
    wordlist = []
    while True:
        lang = input('Please select language (BG-1 / EN-2):')
        if int(lang) in (1,2):
            break
        else:
            print("Enter correct value.")
    lang = int(lang)
    if lang == 1:
        fname = 'words_bg.txt'
        lang_r = 'Bulgarian'
    elif lang == 2:
        fname = '5_list.txt'
        lang_r = 'English'
    with open(fname, 'r') as f:
        wordlist = f.read().splitlines()
        words_lower = [word.lower() for word in wordlist]
    return sorted(set(words_lower)), lang_r


def check_word(str_w, language):
    word_lst = list(str_w)
    if language == 'English':
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    elif language == 'Bulgarian':
        vowels = ['а', 'е', 'и', 'о', 'у', 'ъ', 'ю', 'я']
    vcount = len([l for l in str_w if l in vowels])
    if len(word_lst) != len(set(word_lst)):
        return ''
    elif vcount < 2:
        return ''
    elif vcount >= 2:
        return str_w


def start_with_word():
    word = ''
    while word == '':
        num = randint(0, len(words) - 1)
        word_rnd = words[num]
        print(f'{num} - {word_rnd}')
        suggestion = check_word(word_rnd, language)
        word = suggestion
    return word


def good_word(word_proposed, words_not, words_in, words_correct):
    set_word = list(word_proposed)
    set_words_not = set(words_not)
    set_words_in = set(words_in)
    res = [let for let in set_word if let in set_words_not]
    if len(res) > 0:
        return False
    elif len(set(set_word).intersection(set_words_in)) < len(set_words_in):
        return False
    for pos in words_correct.keys():
        if words_correct[pos] == '_':
            continue
        elif word_proposed[pos-1] != words_correct[pos]:
            return False
    for position, letters in not_in_dict.items():
        for l in letters:
            if word_proposed[position - 1] == l:
                return False
    return True


def propose_words():
    proposed_words = [word for word in words if good_word(word, not_in_word, in_word, correct_word) == True]
    return proposed_words


def count_corrects():
    count = 0
    for letter in correct_word.values():
        if letter != '_':
            count += 1
    return count


# Press the green button in the gutter to run the script.
words, language = open_file()
print(f"Selected language is {language}")

is_cont = False
while is_cont == False:
    start_word = start_with_word()
    q = input(f"Proposed start word is: {start_word}. Do you want to keep it? [Y/N]:")
    if q.lower() == 'y':
        is_cont = True
        print(f"Start with: {start_word}")
        words.remove(start_word)

print('for every character of the word mark it with correct symbol.')
print('N - Not in word')
print('I - in word, other place')
print('C - correct place')

not_in_word = []
in_word = []
correct_word = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_'}
not_in_dict = {1:[], 2:[], 3:[], 4:[], 5:[]}
is_correct = False

correct_count = count_corrects()

while correct_count < len(correct_word.keys()):
    count = 1
    while start_word:
        start_word, letter = start_word[1:], start_word[0]
        while True:
            char = input(f'{letter}: (N,I,C)?:')
            if char.lower() == 'n':
                not_in_word.append(letter)
                if char.lower not in not_in_dict[count]:
                    not_in_dict[count].append(letter)
                break
            elif char.lower() == 'i':
                if letter not in in_word:
                    in_word.append(letter)
                    not_in_dict[count].append(letter)
                break
            elif char.lower() == 'c':
                correct_word[count] = letter
                if letter not in in_word:
                    in_word.append(letter)
                break
        count += 1
    pprint(correct_word.values())
    print(f'Not in word: {not_in_word}')
    print(f'In word: {in_word}')

    proposed = propose_words()
    count_corrects()

    print('\n')
    if len(proposed) == 1:
        print(f'The word is {proposed[0]}')
        break
    print(f'List of proposed words')
    for x,y in enumerate(proposed):
        print(f"{x}: {y}")
    print('Please select word from the list above:')
    print(f'number form 0 to {len(proposed)-1}')
    list_num = int(input())
    start_word = proposed[list_num]
    print(f"Continue with word {start_word}")