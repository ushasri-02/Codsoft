import random
import string

def password(length, uppercase, lowercase, digits, special_chars):
    characters_set = ""
    if uppercase:
        characters_set += string.ascii_uppercase
    if lowercase:
        characters_set += string.ascii_lowercase
    if digits:
        characters_set += string.digits
    if special_chars:
        characters_set += string.punctuation
    
    if characters_set=="":
        print("select at least one character type.")
        return None
    
    password = ''
    for i in range(length):
        password = password+random.choice(characters_set)
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        
        # Prompt the user to select character types
        uppercase = input("1. uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("2. lowercase letters? (y/n): ").lower() == 'y'
        digits = input("3. digits? (y/n): ").lower() == 'y'
        special_chars = input("4. special characters? (y/n): ").lower() == 'y'
        
        gen_pass = password(length, uppercase, lowercase, digits, special_chars)
        print("Generated Password:", gen_pass)
    
    except ValueError:
        print("Please enter a valid integer for the length of the password.")

if __name__ == "__main__":
    main()
