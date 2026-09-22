num1=int(input('please enter a number :'))


num2=int(input('please enter the secend number :'))
num3=int(input('please enter the last number :'))

if num1+num2>num3 and num2+num3>num1 and num1+num3>num2:
    print("this numbers can be used in a triangle")
else:
    print('this numbers cannot be used in a triangle')
