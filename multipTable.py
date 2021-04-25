#!/usr/bin/env python3

#multplication table software

number = [1,2,3,4,5,6,7,8,9,10,11,12]
double_number = []

for num in number:
    double_numbers = num * 2
    double_number.append(double_numbers)
    
    
#The output of this comment code is normal but for the below it, the output is mixed and duplicated of to 12 times
#for lst in double_number:
         
     #print('Multiplication table of two: {}'.format(lst))

for val in number:
    for lst in double_number:
        print('Multiplication table {} {}'.format(val,lst))

   
        
    
