def encoder(plaintext, shift):
    cipher_txt = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                cipher_txt += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                cipher_txt += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher_txt += char
    return cipher_txt
