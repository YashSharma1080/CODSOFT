import string
import random

def password_generator(length):
    characterList = string.ascii_letters + string.digits + string.punctuation
    password = []
    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
    return "".join(password)

length = int(input("Enter password length: "))
print("The random password is ", password_generator(length))