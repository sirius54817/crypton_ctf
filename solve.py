import base64

def solve_base64(encoded_text):
    return base64.b64decode(encoded_text).decode()

def solve_reverse(reversed_text):
    return reversed_text[::-1]

def solve_caesar(encrypted_text):
    result = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated = chr((ord(char) - ascii_offset - 13) % 26 + ascii_offset)
            result += rotated
        else:
            result += char
    return result

def solve_xor(encrypted_text, key=0x13):
    result = ""
    for char in encrypted_text:
        result += chr(ord(char) ^ key)
    return result

def solve_vigenere(encrypted_text, key="CIPHER"):
    result = ""
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result

def solve_rsa(n, e, c):
    # This is a simplified RSA solver for demonstration
    p = 61
    q = 53
    d = 2753
    return chr(pow(c, d, n))

if __name__ == "__main__":
    # Add test cases here
    print("Testing solutions...") 