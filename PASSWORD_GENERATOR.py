

import random
import string

def generate_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))

        if length < 4:
            print("Password length should be at least 4 characters for better security.")
        else:
            new_password = generate_password(length)
            print(f"Your generated password is: {new_password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
main()
