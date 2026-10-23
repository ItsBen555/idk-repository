num = int(input('please enter the number : '))

num=num
while num!=1:
    if num%2==1:
       i = num*3+1
    if num%2==1:
       num=i
    else:
        j = num//2
        num=j
if num==1:
    print(f"the final answer is {num} the theory is working")

else:
    print('are you sure you gave a normall number?? if so the theorys not working')


   
    

    
