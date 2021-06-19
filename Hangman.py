#Hangman game 
import random
# pictorical representation for lifes
stage = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
======
''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
======
''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
======
''','''
 +---+
 |   |
 O   |
 |\  |
     |
     |
======
''','''
+---+
 |   |
 O   |
 |   |
     |
     |
======
''','''
+---+
 |   |
 O   |
     |
     |
     |
======
''','''
+---+
 |   |
     |
     |
     |
     |
======
'''  ]
# list of words from which randomply one word will get selected for play
word_list = ["lovender", "rose", "mango", "pineapple","lotus","orange"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#print(f"Selected word is {chosen_word}\n")
print("Guess the word letter by letter: \n Hint: its either flower or fruit \n")
word_length = len(chosen_word)
display = []
# Put all _ at place of letters in chosen word
for ch in range(word_length):
  display+="_"
print(display)
end_of_game = False
while stage:
  while not end_of_game:
    guess = input("\nGuess letter from word ").lower()
    for position in range(word_length):
      ch = chosen_word[position]
      if ch == guess:
        display[position] = guess
    if guess not in chosen_word:
      while stage:
        print(stage.pop())
        break
      else:
        end_of_game = True
        print("You Loose!!")

    if "_" not in display:
      end_of_game = True
      print(display)
      print("You win!!!")