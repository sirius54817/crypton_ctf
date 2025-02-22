import base64
from cryptography.fernet import Fernet

# Easy Challenges
def create_base64_challenge():
    flag = "CRYPTON{h1dd3n_1n_pl41n_s1ght}"
    return base64.b64encode(flag.encode()).decode()

def create_reverse_challenge():
    flag = "CRYPTON{3s73v37_s1_3m1t}"
    return flag[::-1]

def create_caesar_challenge():
    flag = "CRYPTON{pnrfne_vf_abg_frpher}"
    result = ""
    for char in flag:
        if char.isalpha():
            # ROT13 implementation
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            result += rotated
        else:
            result += char
    return result

# Intermediate Challenges
def create_xor_challenge():
    flag = "CRYPTON{x0r_1s_r3v3rs1bl3}"
    key = 0x13
    result = ""
    for char in flag:
        result += chr(ord(char) ^ key)
    return result

def create_vigenere_challenge():
    flag = "CRYPTON{v1g3n3r3_1s_cl4ss1c}"
    key = "CIPHER"
    result = ""
    key_index = 0
    for char in flag:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result

def create_rsa_challenge():
    p = 61
    q = 53
    n = p * q
    e = 17
    d = 2753  # Pre-calculated private key
    message = "CRYPTON{sm4ll_numb3rs_4r3_w34k}"
    # This is a simplified RSA for demonstration
    return f"n={n}, e={e}, c={pow(ord('C'), e, n)}"

if __name__ == "__main__":
    print("Generating challenges...")
    # Generate all challenges here 