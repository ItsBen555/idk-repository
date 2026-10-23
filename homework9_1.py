
def is_even(num):
    fact=0

    for i in range(2,num):
        if num%i==0:
            fact=+1
    if fact==0:
        return True
    else:
        return False
            


print(is_even(12))
        