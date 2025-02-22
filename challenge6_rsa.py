def create_challenge():
    """Prime Time Challenge"""
    p = 61
    q = 53
    n = p * q
    e = 17
    message = "CRYPTON{sm4ll_numb3rs_4r3_w34k}"
    c = pow(ord('C'), e, n)  # Only encrypting first character for simplicity
    
    question = """
=== Prime Time (300 points) ===

Welcome to your first RSA challenge!
We've intercepted an encrypted message and some parameters.
Can you decrypt it?

Parameters:
n = {}
e = {}
c = {}

Hint: n is a product of two prime numbers less than 100
Additional hint: Try factoring n to find p and q
""".format(n, e, c)
    
    return question, (n, e, c)

if __name__ == "__main__":
    question, answer = create_challenge()
    print(question) 