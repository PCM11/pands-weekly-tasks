# This program reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author Phumi Tshidi

#Ref:https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# Ref:https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/

#import sys.argv to take command line argument

import sys 
while True:
    try:
       filename = sys.argv[1]  
    except IndexError:
        filename = input("Please enter a filename: ")
       #break
    try:
        with open(filename,'r') as f:
            text = f.read()
            count = 0  # counting character "e"
            for i in text:
                if (i == "e" or i =="E"): # count both lower case and upper case
                  count +=1
            print(count)
            break
#sep='' removes blanks before and after filename
    except FileNotFoundError:
                print("filename (", filename,") does not exist. Please  enter a valid filename",sep = '')
                break