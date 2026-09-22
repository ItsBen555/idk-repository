num1=int(input('enter the first number : '))

sign=input('enter the sign you want : ')

num2=int(input('enter the last number : '))

if sign== "*" :
    print(num1*num2)

elif sign== "+":
    print(num1+num2)
elif sign == "-":
    print(num1-num2)

elif sign == "/" :
    print(num1/num2)

elif sign == "//" :
    print(num1//num2)

else:
    print(f"{sign} is not a defined sign")
