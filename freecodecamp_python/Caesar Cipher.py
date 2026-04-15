# Caesar Cipher Implementation
# Encrypts or decrypts text by shifting letters a fixed number of positions in the alphabet

def caesar(text, shift, encrypt=True):
    # Core cipher function used by both encrypt() and decrypt()
    # text: the string to encode or decode
    # shift: how many positions to move each letter in the alphabet
    # encrypt: True means encrypt, False means decrypt

    # Validate that shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validate that shift is within the valid alphabet range (1-25)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define the full lowercase alphabet as our reference
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # For decryption, reverse the shift direction
    if not encrypt:
        shift = -shift

    # Build the shifted alphabet by slicing and rearranging
    # Example with shift=3: 'abcdefghijklmnopqrstuvwxyz'
    #              becomes: 'defghijklmnopqrstuvwxyzabc'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create a translation table that maps every letter to its shifted equivalent
    # Handles both uppercase and lowercase letters
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Apply the translation table to the entire input text
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    # Calls caesar() with default encrypt=True
    return caesar(text, shift)


def decrypt(text, shift):
    # Calls caesar() with encrypt=False to reverse the shift
    return caesar(text, shift, encrypt=False)


# Decrypt a hidden message using a shift of 13 
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
