import os
import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding

# Read the RSA public and private keys from PEM files
with open("public2.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private2.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Plain text to encrypt
plaintext = b"Amjad is here."

# Generate a random AES key
aes_key = os.urandom(32)  # 256-bit key
iv = os.urandom(16)  # 128-bit IV

# Initialize AES encryption
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

# Initialize the padder to add padding to the plaintext
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_plaintext = padder.update(plaintext) + padder.finalize()

# Encrypt the padded plaintext
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

# Encrypt the AES key using the RSA public key
encrypted_aes_key = rsa.encrypt(aes_key, public_key)

# Save the encrypted data, encrypted AES key, and IV to files
with open("encrypted_data.bin", "wb") as f:
    f.write(ciphertext)

with open("encrypted_aes_key.bin", "wb") as f:
    f.write(encrypted_aes_key)

with open("iv.bin", "wb") as f:
    f.write(iv)

print("Sucess")
