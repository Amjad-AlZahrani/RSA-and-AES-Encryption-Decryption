import rsa

# Generate a 2048-bit RSA key pair
public_key, private_key = rsa.newkeys(2048)

# Save the public key in a PEM file
with open("public2.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

# Save the private key in a PEM file
with open("private2.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

print("RSA key saved successfully")
