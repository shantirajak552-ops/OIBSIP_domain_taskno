import string
import random
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
choice = "yes"
while choice == "yes":
    length = int(input("Enter password length: "))
    if length < 6:
        print("Password length must be at least 6.")
    else:
        password=""
        for i in range(length):
            password = password + random.     choice(characters )
        print("password generated:    ",password )    
        choice = input("Do you want to generate another password? (yes/no): ")