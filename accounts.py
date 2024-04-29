# This program reads in a 10 character account number,
# Outputs the account number with only last 4digit showing, and the first 6 digits replaced with Xs)
# Author: Phumi Tshidi

# ref: https://www.tutorialspoint.com/python/index.htm 

# account number: 1234567890

# import random function to generate random account numbers 

import random
import string

account_number = input('Please enter your 10 digit account number:')
last4_digits = account_number[6:]
print (last4_digits)

# replace first 6 digits with 'X'

mask = 6 * str("X")
Final_account = mask + last4_digits
print (Final_account)


# modify program to deal with account numbers of various lengths

new_account_id = ''.join(random.choice(string.digits) for _ in range(12))
print(f"Created account ID: {new_account_id}" )

# print out the last 4digits
# and replace the first 8 digits with 'X'


print(f"Created account ID: {8 * str('X')}{new_account_id[8:]}" )

