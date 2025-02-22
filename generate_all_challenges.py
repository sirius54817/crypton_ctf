import os
from challenge1_base64 import create_challenge as c1
from challenge2_reverse import create_challenge as c2
from challenge3_caesar import create_challenge as c3
from challenge4_xor import create_challenge as c4
from challenge5_vigenere import create_challenge as c5
from challenge6_rsa import create_challenge as c6

def generate_all_challenges():
    # Create challenges directory if it doesn't exist
    if not os.path.exists('challenges'):
        os.makedirs('challenges')
    
    # Generate each challenge
    challenges = [
        ('challenge1.txt', c1()),
        ('challenge2.txt', c2()),
        ('challenge3.txt', c3()),
        ('challenge4.txt', c4()),
        ('challenge5.txt', c5()),
        ('challenge6.txt', c6())
    ]
    
    # Write challenges to files
    for filename, (question, answer) in challenges:
        with open(f'challenges/{filename}', 'w') as f:
            f.write(question)
        
        # Save answers separately for verification
        with open(f'challenges/answers/{filename}', 'w') as f:
            f.write(str(answer))

if __name__ == "__main__":
    generate_all_challenges()
    print("All challenges generated successfully!") 