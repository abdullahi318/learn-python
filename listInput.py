#!/usr/bin/env python3
int_list = []

int_list = input('enter numbers lists: ')
if int_list =="":
    print('-----++++++++++------')
    print('provide input please')
elif int_list != 'abcd':
    print('-----++++++++++++++++------')
    print('provide knowed input please')
else:
    print('-----The is follows:------')
    print(set(int_list))
