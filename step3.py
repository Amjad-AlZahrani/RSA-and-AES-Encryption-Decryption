import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Read the RSA private key from a PEM file
with open("private2.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Read the encrypted data, encrypted AES key, and IV from files
with open("encrypted_data.bin", "rb") as f:
    ciphertext = f.read()

with open("encrypted_aes_key.bin", "rb") as f:
    encrypted_aes_key = f.read()

with open("iv.bin", "rb") as f:
    iv = f.read()

# Decrypt the AES key using the RSA private key
aes_key = rsa.decrypt(encrypted_aes_key, private_key)

# Initialize AES decryption
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()

# Decrypt the encrypted data
decrypted_padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Remove padding from the decrypted plaintext
unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
decrypted_plaintext = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()

# Verify that the decrypted data matches the original plaintext
plaintext = b"wetaan is here."


if decrypted_plaintext == plaintext:
    print("The data is decrypted and the disassembled text is consistent with the original text.")
else:
    print("Data decryption failed and the decrypted text does not match the original text.")
