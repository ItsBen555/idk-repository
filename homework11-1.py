def summm(num1):
    num=int(input('please etner a number : '))
    summ=num1
    while num!=0:
        summ+=num
        
        num=int(input('please enter a number : '))
        if num==5:
            break

    
    return(summ)

print(summm(20))