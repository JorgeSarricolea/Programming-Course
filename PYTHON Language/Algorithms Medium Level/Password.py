# Create a program that generates a random password for the user.
# The password should contain a mix of uppercase and lowercase letters, numbers, and symbols.
# The length of the password should be determined by the user.

import random
import string

def generate_password(length):
    # define characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation

    # generate password
    password = ''.join(random.choice(chars) for i in range(length))

    return password

# get desired password length from user
length = int(input("Enter desired password length: "))

# generate password and print
password = generate_password(length)
print("Your random password is:", password)