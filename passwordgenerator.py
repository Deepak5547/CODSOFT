import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected.")
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired length of the password: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        
        generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        print("Generated Password:", generated_password)
    
    except ValueError as e:
        print(f"Error: {e}")
