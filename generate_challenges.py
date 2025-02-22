import base64
from challenges import *

# Generate all challenges and write to files

def write_challenge_files():
    # 1. Digital Camouflage Challenge
    encoded_flag = create_base64_challenge()
    with open("challenges/camouflage.txt", "w") as f:
        f.write(f"""Welcome to Digital Camouflage!

Can you find the hidden message?

{encoded_flag}
""")

    # 2. Mirror Mirror Challenge
    reversed_flag = create_reverse_challenge()
    with open("challenges/mirror.txt", "w") as f:
        f.write(f"""Welcome to Mirror Mirror!

Something seems backwards here...

{reversed_flag}
""")

    # 3. Emperor's Message Challenge
    caesar_flag = create_caesar_challenge()
    with open("challenges/emperor.txt", "w") as f:
        f.write(f"""Ave Caesar!

The emperor has sent a message:

{caesar_flag}

He mentioned something about rotating letters...
""")

    # 4. Binary Warrior Challenge
    xor_flag = create_xor_challenge()
    with open("challenges/warrior.txt", "w") as f:
        f.write(f"""Welcome to Binary Warrior!

XOR is your friend:

{xor_flag}

Remember: The key is a single byte!
""")

    # 5. Historical Cipher Challenge
    vigenere_flag = create_vigenere_challenge()
    with open("challenges/historical.txt", "w") as f:
        f.write(f"""Welcome to the Historical Cipher!

A message from the past:

{vigenere_flag}

The key to history lies in a simple word...
""")

    # 6. Prime Time Challenge
    rsa_params = create_rsa_challenge()
    with open("challenges/prime.txt", "w") as f:
        f.write(f"""Welcome to Prime Time!

Can you decrypt this RSA message?

{rsa_params}

Remember: p and q are prime numbers less than 100
""")

if __name__ == "__main__":
    write_challenge_files() 