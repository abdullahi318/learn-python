#!/usr/bin/env python

x = int(input("Enter a number to know it factorial:-"))

def fact(x):
        if x > 1: return x * fact(x -1)
        return 1
print("------+++++++++++++++++++++++++++------")
print("The factorial of entered number is: {}\n\n".format(fact(x)))

print("------Counting permutation------\n")
print("The formular is: -- n!/(n-r)! ---\n")
a = int(input("Enter a the first number: "))
b = int(input("Enter a the second number to calculate: "))

#!def pamute(a, b):
        
