def crypt(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  
    return encrypted_message
