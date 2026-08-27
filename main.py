from cryptography.fernet import Fernet

# Skapa en nyckel
key = Fernet.generate_key()

# Skapa ett krypteringsobjekt
cipher = Fernet(key)

# Texten som ska krypteras
text = "Mitt hemliga lösenord"

encrypted = cipher.encrypt(text.encode())

print("Krypterad text: ", encrypted)

# Avkryptera meddelandet
decrypt = cipher.decrypt(encrypted)

print("Avkryppterat meddelande: ", decrypt.decode())


