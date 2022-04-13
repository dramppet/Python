input_choose = input('Please choose a type: ')

if input_choose == '1':
    int_type = int(input('Please enter a int: '))
    print(int_type + 1)
elif input_choose == '2':
    bool_type = input('Please enter a bool: ')
    if bool_type == 'True':
        print('False')
    else:
        print('True')
elif input_choose == '3':
    str_type = input('Please enter a string: ')
    print(str_type + '*')
