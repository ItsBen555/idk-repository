# number=int(input('tell me a number :'))
# flag=0
# for i in range(1,number):
#     if number%i== 0 and i+i+i+i+i+i++i+i+i+i+i+i+i+i+i+i+i+i++i+i+i+i+i+i==number : 
#         flag=flag+1
# if flag > 0:
#     print('number is great')
# else:
#    print('number is not great')
# number=int(input('tell me a number :'))
# flag=0
# for i in range(1,number):
#     if number%i == 0 and i==number: 
#        flag=+1
# if flag!=0:
#    print('number is great')
# else:
#    print(f"{number} is not great")
number=int(input('tell me a number :'))
flag=0
for i in range(2,number):

    if number%i==0:
        flag+=i

if flag==0:
    print('prime number')
else:
    print('you dumb')       




