# this program takes a positive floating point number,
# as an input and prints out the approximate square root,
# using Newtons method.

# ref: https://en.wikipedia.org/wiki/Newton's_method
# ref: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# author - Phumi Tshidi

def sqrt_float(num):
    # initial guess for the square root
     guess = num/2.0
    
     # new guess for the square root
     while True:
         new_guess = (guess + num /guess)/2.0

         # Adjust tolerance for accuracy

         if abs(new_guess - guess) < 0.00001:
          return new_guess
         guess = new_guess

num =float(input("Please enter a positive integer: "))
print(sqrt_float(num)) 
