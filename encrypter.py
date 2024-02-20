import cryptocode
import sys

def encrypt(key, data):
    print("Clave crifrada:")
    print(cryptocode.encrypt(str(data),str(key)))

def decrypt(key, data):
    print("Clave descrifrada:")
    print(cryptocode.decrypt(str(data),str(key)))

action = input("Type 1 for encrypt or 2 for decrypt:")
key = input("Write the password:\n")
data = input("Write the data you want to convert:\n")
if action == str(1):
    encrypt(key, data)
elif action == str(2):
    decrypt(key, data)    
