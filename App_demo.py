#!/usr/bin/env python3

    #variable delaration
names = []
address = []
age = []
institute = []
dept = []

        

print('------+++++++Welcome to student info software+++++++------\n')
names.insert(0, input('Enter your Full name: '))
address.insert(0, input('Enter your Address: '))
age.insert(0, input('Enter your Age: '))
institute.insert(0, input('Enter your School: '))
dept.insert(0, input('Enter your Departiment: '))
print('\n\n')
    

print('-----+++++Your information is below+++++-----\n')
print("Name is: {} \nAddress is: {}  \nAge is: {} \nInstitute is: {} \nDept is: {}".format(names,address,age,institute,dept))
