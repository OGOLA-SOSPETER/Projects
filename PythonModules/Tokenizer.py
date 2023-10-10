#Tokenization.
#Random password generator
import encodings.utf_8
import random

import bcrypt

password = input('Enter Password: ')

password1 = password.lower()

encrypted_password = bcrypt.hashpw(password.encode(),salt=bcrypt.gensalt(12,b"2b"))
print(f'Your password = {encrypted_password}')



for count in range(len(password)):
    token = random.shuffle
