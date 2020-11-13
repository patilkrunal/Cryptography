from Encrypt import *
from Decrypt import *
from Keygenerator import *

e=Encrypt()
k=Keygenerator()
d=Decrypt()

string_to_be_encoded = "Hello!! This is my cryptography program."
print("Original  : ",string_to_be_encoded)
key=k.generatekey(string_to_be_encoded)
encrypted_string = e.encrypt(string_to_be_encoded,key)
print("Encrypted : ",encrypted_string)
decrypted_string = d.decrypt(encrypted_string,key)
print("Decrypted : ",decrypted_string)