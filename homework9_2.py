num=int(input('please enter a number : '))

def perfect_number(num):
    perfectNumber=0
    for i in range(1,num):
        if num%i==0:
            perfectNumber+=i
    if perfectNumber==num:
        return True
    else:
        return False

print(perfect_number(num))


