#!/usr/bin/env python3

    fact(number):
    
    if number > 1:
        return number * fact(number-1)
    return 1
fact(number = input('Enter a number :'))

