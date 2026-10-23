num=int(input('please enter a number : '))

def reversed_num(num):
    reversedNUm=0
    while num!=0:
        reversedNUm*=10
        reversedNUm=num%10+reversedNUm#321
        num=num//10  
    return reversedNUm

print(reversed_num(num))