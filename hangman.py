stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


word_list = [
    'action',
    'apple',
    'angel',
    'adopted',
    'adult',
    'bicycle',
    'butterfly',
    'bisexual',
    'bikini',
    'crypto',
    'cock',
    'condom',
    'feminist',
    'female',
    'woman',
    'human',
    'anonymous',
    'vagina',
    'boobs',
    'lesbian'
]


import random
from replit import clear

print(logo)
finish_game = False
lives = len(stages) - 1
chosen_word = random.choice(word_list)
w_length = len(chosen_word)
display = []
for i in range(w_length):
    display += '_'
print(display)
while not finish_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(w_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            finish_game = True
            print("You Lose!")
    if not '_' in display:
        finish_game = True
        print("You Win!")
    print(stages[lives])

