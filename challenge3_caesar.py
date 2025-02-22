def create_challenge():
    """Emperor's Message Challenge"""
    flag = "CRYPTON{pnrfne_vf_abg_frpher}"
    encrypted = ""
    
    # ROT13 encryption
    for char in flag:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            encrypted += rotated
        else:
            encrypted += char
    
    question = """
=== Emperor's Message (150 points) ===

Julius Caesar left us a message using his favorite encryption method.
All letters have been shifted by the same amount.

Encrypted message:
{}

Hint: The emperor really liked the number 13
""".format(encrypted)
    
    return question, encrypted

if __name__ == "__main__":
    question, answer = create_challenge()
    print(question) 