text = input("Enter text: ")
encrypt_text=""
flag = False

def ceaser_encrypt(text, key):
    result =""
    text = text.upper()
    for char in text:
        if char.isalpha():
            base =  ord('A')
            result += chr((ord(char) -base +  key) % 26 + base)
        else:
            result += char
    return result

def ceaser_decrypt(encrypt_text, key):
    result=""
    encrypt_text = encrypt_text.upper()
    for char in encrypt_text:
        if char.isalpha():
            base = ord('A')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result

while(True):
    print("1.Encrypt\n2.Decrypt\n3.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        flag = True
        key = int(input("Enter key (number): "))
        encrypt_text = ceaser_encrypt(text, key)
        print("Encrypted Text: ", encrypt_text)
    elif choice == 2:
        if flag:
            decrypt_text = ceaser_decrypt(encrypt_text, key)
            print("Decrypted Text: ", decrypt_text)
        else:
            print("Please encrypt the text first.")
    elif choice == 3:
        break