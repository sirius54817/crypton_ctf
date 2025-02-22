import base64

def create_challenge():
    """Digital Camouflage Challenge"""
    flag = "CRYPTON{h1dd3n_1n_pl41n_s1ght}"
    encoded = base64.b64encode(flag.encode()).decode()
    
    question = """
=== Digital Camouflage (100 points) ===

Someone intercepted this message, but it looks like gibberish.
Our analysts say it's using a common encoding method often seen in email attachments.
Can you decode it and find the flag?

Encrypted message:
{}

Hint: This encoding uses 64 different characters and often ends with = or ==
""".format(encoded)
    
    return question, encoded

if __name__ == "__main__":
    question, answer = create_challenge()
    print(question) 