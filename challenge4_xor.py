def create_challenge():
    """Binary Warrior Challenge"""
    flag = "CRYPTON{x0r_1s_r3v3rs1bl3}"
    key = 0x13
    encrypted = ""
    
    # XOR encryption
    for char in flag:
        encrypted += chr(ord(char) ^ key)
    
    question = """
=== Binary Warrior (200 points) ===

This message has been XORed with a single byte key.
The key is somewhere between 0x00 and 0xFF.

Encrypted message:
{}

Hint: XOR is its own inverse operation
Additional hint: key = 0x13
""".format(encrypted)
    
    return question, encrypted

if __name__ == "__main__":
    question, answer = create_challenge()
    print(question) 