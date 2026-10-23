num=int(input('please enter a number : '))
additionOfNumber=0
while num!=0:
    additionOfNumber=num%10+additionOfNumber
    num//=10
print(f"addition of the number you gave is equal to {additionOfNumber}")