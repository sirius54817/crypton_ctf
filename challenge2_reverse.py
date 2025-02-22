def create_challenge():
    """Mirror Mirror Challenge"""
    flag = "CRYPTON{3s73v37_s1_3m1t}"
    reversed_flag = flag[::-1]
    
    question = """
=== Mirror Mirror (100 points) ===

We found this message, but it seems to be backwards.
Can you help us read it correctly?

Message:
{}

Hint: Sometimes you need to look at things from a different perspective
""".format(reversed_flag)
    
    return question, reversed_flag

if __name__ == "__main__":
    question, answer = create_challenge()
    print(question) 