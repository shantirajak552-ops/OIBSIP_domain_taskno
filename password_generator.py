import string
import random
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

length = int(input("Enter password length: "))
password=""
for i in range(length):
    password = password + random.choice(characters )
print("password generated:    ",password )    