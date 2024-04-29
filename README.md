# Pands-weekly-tasks

## Problem Sheet 2024

This repository contains weekly problem tasks for semester 1 of Programming and Scripting Module for Higher Data Analytics course offered by ATU Galway.

It contains intructions and a brief explanation about each program.

## Requirements

I used python to create the programs, and it can be installed by downloading [anaconda](https://www.anaconda.com/download).
I also used a notebook editor which can be accessed through [Visual Studio Code](https://code.visualstudio.com/) installation.

## Programs

## 1. Helloworld.py

This program displays "Hello World! when it is run.

## 2. Bank.py

*Write a program called bank.py which prompts the user and read in two money amounts (in cent); adds the two amounts and prints out the answer in a format with a euro sign and decimal point between the euro and cent of the amount.*

This program prompts the user to enter two amount of money in cents.
Add the the two amounts and print it in Euro an cent amount.

Instruction:
    Enter amount1(in cent): 65
    Enter amount2(in cent): 180

Expected output:
    The sum of these is €2.45

## 3.Accounts.py

*Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).*

This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
It is then modified to deal with account number

Instruction:
    Please enter an 10 digit account number: 1234567890
    Modify the program to deal with account numbers of any length.

Expected output:
    XXXXXX7890

## 4.Collatz.py

*Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.*

This program asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step it calculates the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
More details about the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) can be found on wikipedia.

Instruction:
    Please enter a positive number: 10

Expected output:
    10 5 16 8 4 2 1

## 5. Weekday.py

*Write a program that outputs whether or not today is a weekday.*

 Expected Output:
    If the program is run on a weekday it prints " Yes, unfortunately today is a weekday".
    If it's run on a weekend it prints out " It is the weekend yay!"

## 6.Es.py

*Write a program that reads in a text file and outputs the number of e's it contains, document any assumptions you are making. The program should take the filename from an argument on the command line.*

This program takes in the filename from an argument on the command line and reads out the number of e's it contains.

Expected Output:
  116960

## 7.Squareroot.py

*Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this and should not use the built in functions x ** .5 >or math.sqrt(x).*

This program creates a code that estimates a square root of a number by applying [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method), without using the built in square root functions "x**o.5 or math.sqrt(x)".

Instruction:
    Please enter a positive number: 14.5

Expected output:
    The square root of 14.5 is approx. 3.8.

## 8.Plottask.py

*Write a program called plottask.py that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range to 10, on the one set of axes.*

This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range 0 to 10, on one set of axes.
