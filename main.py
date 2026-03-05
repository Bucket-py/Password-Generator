from random import randint

def main():
    print("------------------------")
    print("Password Generator")
    print("------------------------")
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
    print("Do you want to copy this to your clipboard? (y/n)")
    
    if input().lower() == 'y':
        copy_to_clipboard(password)
        print("Password copied to clipboard!")
    else:
        print("Password not copied to clipboard.")

    print("Do you want to save this password to a text file? (y/n)")
    if input().lower() == 'y':
        make_txt_file(password)
    else:
        print("Password not saved to text file.")
        
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for _ in range(length):
        password += characters[randint(0, len(characters) - 1)]
    return password

def copy_to_clipboard(password):
    try:
        import pyperclip
        pyperclip.copy(password)
        print("Password copied to clipboard!")
    except ImportError:
        print("pyperclip module not found. Please install it to enable clipboard functionality.")
        
def make_txt_file(password):
    with open("password.txt", "w") as file:
        file.write(password)
    print("Password saved to password.txt")

if __name__ == "__main__":
    main()
