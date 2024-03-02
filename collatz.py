# this program asks the user to input any positive integer,
# and outputs the successive values until it reaches one.
# ref: Real Python, stackoverflow.com
# author: Phumi


# it divides even numbers by 2
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    
    # multiplies odd numbers by 3 and add 1
    elif number % 2 == 1:
        print (3 * number + 1)
        return ( 3 * number +1 )
    
    
number = input("Please enter a positive integer: ")

# loop continues until the answer is 1.
while number !=1:
    number = collatz(int(number))


        
    


