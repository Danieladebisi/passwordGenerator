import random

print('Welcome to password generator')
chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

number = input('Amount of password to generate: ')
number = int(number)

length = input('input your password length: ')
length = int(length)

print('Here are your passwords: ')

for pwd in range(number):
    passwords= ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)