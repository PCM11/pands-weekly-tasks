#  this program displays a histogram of a normal distribution
# and a plot of the function  h(x)=x3  
# author Phumi Tshidi
# ref: W3 Schools, geeksforgeeks.org

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
data = np.random.normal(5.0, 2.0, 1000)
 # this will give us the array with 1000 values 

# Define the function h(x) = x^3
def h(x):
   return x ** 3

# Generate a range of x values
x = np.linspace(0, 10)

# Plot the histogram and function and save the figure.
plt.hist(data, label= 'NormData')
plt.plot(x, h(x), label = 'h(x) = x^3')
plt.title('NormData and Function')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid("True")
plt.legend()
plt.savefig("Function.png")
plt.show()