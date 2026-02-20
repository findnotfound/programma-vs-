import random


Chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = input("Quanto vuoi che sia lunga la password: ")

password = ""

for i in range(int(long)):
    generator = random.choice(Chars)
    password += generator

print("La password è: " + password)

