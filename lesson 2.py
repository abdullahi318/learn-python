#!/usr/bin/env python3

firstName = 'Abdullahi'
lastName = 'Salihu'

name = input('Enter your first name :')

lname = input('Enter your last name :')

if name == ""  or lname == "":
    print('Provide input please')
if name == firstName and lname == lastName:
    print('Your full name is correct')
else:
    print('Your full name is incorrect')

    



