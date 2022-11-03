
import words
import random
from words import words

def list_duplicates_of(seq,item):
    start_at = -1 # 1
    locs = [] # 1, 
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc 
    return locs

def hangman():

    secret_word = random.choice(words) # pick secret word

    u_secret_word = secret_word.upper()
    
    lives = 7 # Lives counter

    split_sw = list(u_secret_word) # make a list of the secret word
    
    sw_counter = len(u_secret_word) # Count characters in split_sw

    underscore_word = sw_counter * "_" # Make a second variable with the equal of the word with "_"

    underscore_word_list = list(underscore_word) # Make a list of the undersocre word for be able to update

    underscore_word_string = "".join(underscore_word_list) # Put characters together post update
    
    u_l = [] # Used letters

    #print(secret_word) 
    

    while lives > 0 or underscore_word == u_secret_word: 
    
        
        u_pick = str.upper(input(f"Guess the secret word: {underscore_word_string}, you have {lives} lifes, Lletters used:{u_l} \n enter your chosen letter: "))
        
        if u_pick in u_l :
            print("You already pick this letter, please pick another one")
            continue

        indexes = list_duplicates_of(u_secret_word, u_pick)
        u_l.append(u_pick)
        if u_pick in split_sw:
            
            u_pick_index = split_sw.index(u_pick)
            for e in indexes:
                underscore_word_list[e]  = u_pick

            underscore_word_string = "".join(underscore_word_list) # Put characters together post update
            
            if underscore_word_string == u_secret_word:
                print(f"You won!, the secret word is {u_secret_word}, total lives: {lives} ")
                break
            #if u_pick in underscore_word_string and u_l and split_sw:
                #print("You already pick this letter, please pick another one")

            print(f"Correct!, {u_pick} is in the word")

        elif u_pick is not split_sw : #and u_pick is not u_l :

            #if u_pick is not u_l:
                #print("You already pick this letter, please pick another one")

            if u_pick is not u_l:
                print(f"Wrong, {u_pick} is not in the word ")
                lives -= 1
            
        
   
    if lives == 0 :
        print(f"You lose, the secret word is {u_secret_word}")
    
            
hangman()
