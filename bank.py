# Bank.py
# Progaram that prompts the user and read in two money amounts (in cents).
# It then add the two amounts,
# Then print out the answer in euro sign and decimal point between the euro and the cent amount.

# Author: Phumi Tshidi

# First amount(in cents) = 65
# Second amount (in cents) = 180

amount1 = input('Enter amount1: ')
amount2 = input('Enter amount2: ')
Totalamount = int(amount1) + int(amount2)
print(Totalamount)

# divive Totalamount by 100 to convert cents to euros

Finalsum = Totalamount / 100
print('€',Finalsum)