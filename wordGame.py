#this is from Day7 of course 100 Days of Code: The Complete Python Pro Bootcamp by by Dr. Angela Yu as found on Udemy 
#this file needs some work but it is my first attempt prior to seeing final version from the instructor.
import random
import os
from hangman_words import word_list

from art import stages, logo
#bank=["subway", "abruptly", "bandwagon", "microwave", "peekaboo", "pajama", "wave", "jackpot", "money", "buffalo", "buzzard", "kazoo"]
chosen_word=random.choice(word_list)
#delete/(or comment out) once game play is proven:
print(f"psst the word is: {chosen_word}")
list_spaces=[]
for char in chosen_word:
    list_spaces+="_"
print(logo)
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
    if guess in list_spaces:
        print(f"you have already choosen the letter {guess}")
    
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            list_spaces[position]=letter
            print(logo)
            print(list_spaces)
            print(f"your current guessed letters are: {guessed_letters}")
    if "_" not in list_spaces:
        end_of_game=True
    if guess not in chosen_word:
        health-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"You guessed {guess}, that is not in the word. You loose a life")
        print(logo)
        print(stages[health])
        print(list_spaces)
        print(f"your current guessed letters are: {guessed_letters}")
        if health==0:
            end_of_game=True

if health>0:
    print("You won!")
else:
    print("Game over, thanks for playing!")
