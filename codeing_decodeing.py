import random

def generate_prefix():
    prefix = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3))
    return prefix

def generate_suffix():
    suffix = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3))
    return suffix

def encode_word(word):
    prefix = generate_prefix()
    suffix = generate_suffix()
    new_word = prefix + word + suffix
    return new_word

def encode_message(msg):
    encoded = [encode_word(word) for word in msg]
    return " ".join(encoded)

def decode_word(word):
    if len(word) >= 6:
        decoded_word = word[3:-3]
        return decoded_word
    else:
        return word[::-1]

def decode_message(msg):
    decoded = [decode_word(word) for word in msg]
    return " ".join(decoded)

while True:
    print("Welcome to the Codeword Converter !")
    print("You can choose ...")
    print("1. for Encode a message")
    print("2. for Decode a message")
    print("3. for Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        user_input = input("Enter the message to encode: ")
        words = user_input.split()
        encoded_message = encode_message(words)
        print("Encoded Message: " + encoded_message)
    elif choice == "2":
        user_input = input("Enter the message to decode: ")
        words = user_input.split()
        decoded_message = decode_message(words)
        print("Decoded Message: " + decoded_message)
    elif choice == "3":
        print("Thank you for using the Codeword Converter!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
