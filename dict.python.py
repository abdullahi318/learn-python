#!/usr/bin/env python3

#Company staff record software
print('='*35)
print('Company staff record software v1.o'.upper())
print('*'*35)
print()

print('\tMAIN MENU ')
print('*' * 30)
print('1 - Add a staff')
print('2 - Update a staff')
print('3 - Delete a staff')
print('4 - Display a staff')
print('5 - Exit software')
print()


#A fuction include switch statement of the software modules
def softwareMod(num):
    switcher = {
        0:
        1:
        2:
        3:
        4:
        5:
        }

        #adding record section
print('='*20)
print('Add staff record')
print('*'*20)
company = {
    'name: ': input("Enter your name: "),
    'state: ':input("Enter your state: "),
    'lga: ':  input("Enter your L G A: "),
    'inst: ': input("Enter your Institute: "),
    'dept: ': input("Enter your Dept: ")

    }
print('record added successful')
print()
print()
#print("==========++++++++++++++=========")
#for x in company.values():
    #print("|%s|" % (x.ljust(10-len(x))))
    #print("+++++++++++++++++++++++++++++++++")
   



        #update record section
print('='*20)
print('Upadate staff record')
print('*'*20)
company.update({
    'name: ': input("Enter your name: "),
    'state: ': input("Enter your state: "),
    'lga: ': input("Enter your L G A: "),
    'inst: ': input("Enter your Institute: "),
    'dept: ': input("Enter your Dept: ")
    })
print('record updated successful')



#delete record section
print('='*20)
print('Delete staff record')
print('*'*20)
print()
company.clear()



        #diplay record section
print('='*20)
print('Display staff record')
print('*'*20)
print()
print()
print("==========++++++++++++++=========")
for x in company.values():
    
    print("|%s|" % (x.ljust(10-len(x))))
    print("+++++++++++++++++++++++++++++++++")




       
