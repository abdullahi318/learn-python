#!/usr/bin/env py00thon3


def weerk(num):
        switcher={
                0:'sunday',                        


#print('='*20)
#print('Add staff record')
#print('*'*20)
#company = {
    #'name: ': input("Enter your name: "),
    #'state: ':input("Enter your state: "),
    #'lga: ':  input("Enter your L G A: "),
    #'inst: ': input("Enter your Institute: "),
    #'dept: ': input("Enter your Dept: ")

    #}
#print('record added successful')
#print()                
                
                
                1:'Monday',
                2:'Tuesday'
                }
        return switcher.get(num)
        
            
        
num = int(input('Enter a day: '))
          
if num == 0:
        print("The day is: "+weerk(0))

        
elif  num == 1:
        print('The day is: '+weerk(1))


elif num == 2:
        print('The day is: '+weerk(2))

elif num == 5:
        print('Good bye:')
        

#while num > 4:
        #print("Invalid entry: ")
        #print()
        
        
        
    
       


    
    

     
