def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                result += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            result += char
    return result

def encrypt_message(message, shift):
    return caesar_cipher(message, shift)

def decrypt_message(encrypted_message, shift):
    return caesar_cipher(encrypted_message, -shift)

if __name__ == "__main__":
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ").lower()
    
    if choice == 'e':
        message = input("Enter the message you want to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt_message(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'd':
        encrypted_message = input("Enter the message you want to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt_message(encrypted_message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
