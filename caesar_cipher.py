# caesar_cipher.py
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("Encrypt or Decrypt (e/d): ").lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))
    if choice == "e":
        print("Encrypted:", caesar_encrypt(text, shift))
    else:
        print("Decrypted:", caesar_decrypt(text, shift))
