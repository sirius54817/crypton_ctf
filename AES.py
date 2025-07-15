from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_key(key_size=256):
    """
    Generate a random AES key of specified size.
    
    Args:
        key_size (int): Key size in bits (128, 192, or 256)
    
    Returns:
        bytes: Random key
    """
    # Convert bits to bytes (8 bits = 1 byte)
    key_bytes = key_size // 8
    return os.urandom(key_bytes)

def encrypt_aes(plaintext, key, mode="CBC"):
    """
    Encrypt data using AES.
    
    Args:
        plaintext (str or bytes): The data to encrypt
        key (bytes): The encryption key
        mode (str): The encryption mode (CBC, ECB, CTR, GCM)
    
    Returns:
        dict: Dictionary containing iv and encrypted data in base64
    """
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # Create an initialization vector
    iv = os.urandom(16)
    
    # Apply padding
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    
    # Choose mode
    if mode == "CBC":
        cipher_mode = modes.CBC(iv)
    elif mode == "ECB":
        cipher_mode = modes.ECB()
        iv = None
    elif mode == "CTR":
        cipher_mode = modes.CTR(iv)
    elif mode == "GCM":
        cipher_mode = modes.GCM(iv)
    else:
        raise ValueError(f"Unsupported mode: {mode}")
    
    # Create encryptor
    encryptor = Cipher(
        algorithms.AES(key),
        cipher_mode,
        backend=default_backend()
    ).encryptor()
    
    # Encrypt the data
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    # Return results
    result = {
        'ciphertext': base64.b64encode(ciphertext).decode('utf-8')
    }
    
    if iv:
        result['iv'] = base64.b64encode(iv).decode('utf-8')
    
    if hasattr(encryptor, 'tag'):  # For GCM mode
        result['tag'] = base64.b64encode(encryptor.tag).decode('utf-8')
    
    return result

def decrypt_aes(encrypted_data, key, mode="CBC"):
    """
    Decrypt AES encrypted data.
    
    Args:
        encrypted_data (dict): Dictionary containing iv and encrypted data
        key (bytes): The encryption key
        mode (str): The encryption mode (CBC, ECB, CTR, GCM)
    
    Returns:
        bytes: Decrypted data
    """
    # Decode base64
    ciphertext = base64.b64decode(encrypted_data['ciphertext'])
    iv = base64.b64decode(encrypted_data['iv']) if 'iv' in encrypted_data else None
    tag = base64.b64decode(encrypted_data['tag']) if 'tag' in encrypted_data else None
    
    # Choose mode
    if mode == "CBC":
        cipher_mode = modes.CBC(iv)
    elif mode == "ECB":
        cipher_mode = modes.ECB()
    elif mode == "CTR":
        cipher_mode = modes.CTR(iv)
    elif mode == "GCM":
        cipher_mode = modes.GCM(iv, tag)
    else:
        raise ValueError(f"Unsupported mode: {mode}")
    
    # Create decryptor
    decryptor = Cipher(
        algorithms.AES(key),
        cipher_mode,
        backend=default_backend()
    ).decryptor()
    
    # Decrypt the data
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext

# Example usage
if __name__ == "__main__":
    # Generate a random 256-bit key
    key = generate_key(256)
    print("Key (base64):", base64.b64encode(key).decode('utf-8'))
    
    # Original message
    message = "somanadh"
    print("Original message:", message)
    
    # Encrypt using AES-CBC (default)
    encrypted = encrypt_aes(message, key)
    print("\nEncrypted (CBC):")
    print("IV:", encrypted.get('iv', 'N/A'))
    print("Ciphertext:", encrypted['ciphertext'])
    
    # Decrypt
    decrypted = decrypt_aes(encrypted, key)
    print("\nDecrypted message:", decrypted.decode('utf-8'))
    
    # Example with different modes
    print("\n--- Different Modes ---")
    modes = ["CBC", "ECB", "CTR", "GCM"]
    
    for mode in modes:
        try:
            print(f"\nMode: {mode}")
            encrypted = encrypt_aes(message, key, mode)
            decrypted = decrypt_aes(encrypted, key, mode)
            print(f"Successfully encrypted and decrypted using AES-{mode}")
        except Exception as e:
            print(f"Error with {mode}: {e}")