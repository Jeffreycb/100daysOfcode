#project from 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu through Udemy 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift):
    altered_word=''
    for item in message:
        letter= alphabet.index(item)
        new_position=letter+shift
        altered_word += alphabet[new_position]
    print (altered_word)

def decode(message, shift):
    decoded_word=''
    for item in message:
        letter= alphabet.index(item)
        new_position=letter-shift
        decoded_word += alphabet[new_position]
    print (decoded_word)
#defined aspects are above /// user imput is below
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message= input(f"Hey what word do you want to {direction}?\n").lower()
shift= int(input("Hey what amount do you want to shift? enter a number please\n"))

if direction=='encode':
    encode(message, shift)
elif direction =='decode':
    decode(message, shift)
else:
    print(f"Sorry {direction} is not a function yet please try again.")
