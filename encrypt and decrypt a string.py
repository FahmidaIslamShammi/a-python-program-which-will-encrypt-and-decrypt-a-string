import cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
message=input("Enter the message you want to send :\n")
converted_message = bytes(message, 'utf-8')
encrypted_message = f.encrypt(converted_message)
print("Your encrypted message: ", encrypted_message.decode())
decrypted_message = f.decrypt(encrypted_message)
print("Your real message after decryption: ",decrypted_message.decode())