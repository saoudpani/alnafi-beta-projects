#!/usr/bin/env python3

#this is simple hangman game with 7 chances to score and the words are retrieved form datamuze API

#important packages 
#from IPython.display import clear_output
import Draw_Hangman as hangman
import requests, os, glob, random

#defining datamuse function to retrive words from datamuse API
def datamuse(word):
    try:
        base_url = 'https://api.datamuse.com/words'
        params_dict = {}
        params_dict['rel_trg'] = word
        response = requests.get(base_url, params=params_dict)
        if response.status_code == 200:
            return [w['word'] for w in response.json()]  #return a list of words from matching category
        else:
            return 404  #in case of faliure
    except:
        return 404  #in case of faliure

# define our clear function 
def clear(): 
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux
    else: 
        _ = os.system('clear') 
        
#game logic is defined in this function     
def game_logic(getword):
    word = [x.lower() for x in getword]
    guess_word = ['_' for i in range(len(word))]
    [print(x, end=" ") for x in guess_word]
    #console
    turns, guessed_char_list = 0, []
    state = hangman.HANGMANPICS[0]
    while True:
        char = input('\nGuess a character:')
        clear()
        if char in guessed_char_list:
            print(f'"{char}" is already guessed, {7-turns} turns remaining.')
            [print(x, end=" ") for x in guess_word]
            print(state)
        else:
            guessed_char_list.append(char)
            if char in word:
                print(f"Hurrah! '{char}' is found in a word, {7-turns} turns remaining.")
                for i in range(len(word)):
                    if word[i] == char:
                        guess_word[i] = char
                [print(x, end=" ") for x in guess_word]
                print(end='\n')
                print(state)
            else:
                turns+=1
                print(f"Sorry! '{char}' is not found in a word, {7-turns} turns remaining.")
                [print(x, end=" ") for x in guess_word]
                state = hangman.HANGMANPICS[turns-1]
                print(hangman.HANGMANPICS[turns-1])
        
        if word == guess_word:
            print('Congrats, You Guessed Right Word: ',"".join(guess_word))
            break
        if turns == 7:
            print("\nFailed! Dont Worry Try Again")
            break
            
#storing and fetching words from word_corpus directory
print("----------WELCOME TO HANGMAN BY SAOUD PANEZAI----------\n") 
print("|Select any category (i.e. sports, country name, hobbies etc|")
cat = input("ENTER CATEGORY NAME or SELECT FROM FILE RANDOMLY BY ENTER BLANK:").lower()
check = 'ok'
del_cat = ''
wordlist = []
def open_word_corpus(c):
    with open('word_corpus/'+c+'.txt') as file:
        return [word.strip() for word in file.readlines()]
    
if os.path.exists('word_corpus/'+cat+'.txt'):
    wordlist = open_word_corpus(cat)
else:
    if datamuse(cat) == [] or datamuse(cat) == 404:
        random_cat = [file[12:-4] for file in glob.glob('word_corpus/*.txt')]
        random.shuffle(random_cat)
        old_category = random_cat[0]
        print(f'API failed to retrive data so random category is: "{old_category}"')
        wordlist = open_word_corpus(old_category) 
    else:
        with open('word_corpus/'+cat+'.txt', 'w') as file:
            del_cat = cat
            for w in datamuse(cat):
                file.writelines(w+'\n')
        wordlist = open_word_corpus(cat)
        
#main game execution
while True:
    if check == 'ok':
        clear()
        random.shuffle(wordlist)
        word = wordlist[0]
        print('*************Let Us Begin The Fun************')
        game_logic(word)
    else:
        print('Bye Bye see you again!')
        if del_cat != '':
            os.remove('word_corpus/'+del_cat+'.txt')
            print(del_cat+'.txt removed')
        break
    check = input('Enter "ok" to Guess another word: ')
