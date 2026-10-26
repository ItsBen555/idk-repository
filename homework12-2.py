import random as rs
number=rs.randint(1,50)

print(number)

numInput=int(input('please enter the number u choose (1,50) :'))
try:
    for i in range(1,50):
        if numInput>number:
            print('the number u gave was too big try again')
            numInput=int(input('please enter the number u choose (1,50) :'))

        elif numInput<number:
            print('yeah still lower than the number given ')
            numInput=int(input('please enter the number u choose (1,50) :'))
        else:

            print(f'finally u are correct te number is {number} and u choosed {numInput}')
            break
except:
    print('make sure it was an int not float or an str and then restart')

# try:
#     if numInput==number:
#         print('u found the number!!!')
#     elif numInput>number:
#         print('the number u gave was bigger than normal ):')
#     else:
#         print('the number u gave was lower than the actuall number lets try again')

# except:
#     print('make sure ur number is a int not float or anythin else')

# finally:
    
          
#     if numInput>number or number>numInput:
#         numInput=int(input('once again enter a number :'))