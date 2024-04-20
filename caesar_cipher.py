#project from 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu through Udemy 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message= input(f"Hey what word do you want to {direction}?\n").lower()
shift= int(input("Hey what amount do you want to shift? enter a number please\n"))
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for item in start_text:
        letter = alphabet.index(item)
        new_position = letter + shift_amount
        end_text += alphabet[new_position]
    print(end_text)
caesar(start_text=message, shift_amount=shift, cipher_direction=direction)
