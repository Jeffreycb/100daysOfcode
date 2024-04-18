#this is from Day7 of course 100 Days of Code: The Complete Python Pro Bootcamp by by Dr. Angela Yu as found on Udemy 
#this file needs some work but it is my first attempt prior to seeing final version from the instructor.
import random
bank=["subway", "abruptly", "bandwagon", "microwave", "peekaboo", "pajama", "wave", "jackpot", "money", "buffalo", "buzzard", "kazoo"]
chosen_word=bank[random.randint(0,len(bank)-1)]
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
print(chosen_word)
list_spaces=[]
for char in chosen_word:
    list_spaces+="_"
print(stages[6])
print(list_spaces)
guess=""
guessed_letters=""
#player health
health=5
end_of_game=False

while end_of_game!=True and health>0:
    guess=input("please choose a letter to guess the word\n").lower()
    guessed_letters+=guess
    
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            list_spaces[position]=letter
            print(list_spaces)
            print(f"your current guessed letters are: {guessed_letters}")
    if "_" not in list_spaces:
        end_of_game=True
    if guess not in chosen_word:
        health-=1
        print(stages[health])
        print(list_spaces)
        print(f"your current guessed letters are: {guessed_letters}")

        if health==0:
            end_of_game=True
if health>0:
    print("You won!")
else:
    print("Game over, thanks for playing!")
