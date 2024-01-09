"""
notice alphabet has two sets of a-z to account for near end letters
"""


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# check if user made a valid 'direction' input
if direction != 'encode' and direction != 'decode':
    print("Invalid cipher choice, type 'encode' or 'decode'")
    exit()

# other inputs
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")


# Test run
caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
