def create_challenge():
    """Historical Cipher Challenge"""
    flag = "CRYPTON{v1g3n3r3_1s_cl4ss1c}"
    key = "CIPHER"
    encrypted = ""
    key_index = 0
    
    # Vigenère encryption
    for char in flag:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted += char
    
    question = """
=== Historical Cipher (250 points) ===

This message was encrypted using a 16th-century polyalphabetic cipher.
The key is a 6-letter word related to encryption.

Encrypted message:
{}

Hint: The key word is hidden in plain sight
Additional hint: Think about what we use to encrypt messages
""".format(encrypted)
    
    return question, encrypted

if __name__ == "__main__":
    question, answer = create_challenge()
    print(question) 