number=int(input("please enter a number :"))
alist=[]


number2=int(input('please enter the secend number :'))

if number2<number:
    number=number2

for i in range(2,3): 
    for j in range(number+1,number2):  #3,4
        if j==1:
            alist.append(j)
        if j>i and j%i!=0 : 
            alist.append(j)
    
            




print(alist)
# number=int(input("please enter a number :"))
# flag=0
# for i in range(2,number):

#     if number%i==0:
#         flag=flag=+1
 
        

# if flag>0:
#     print('number is not first')
# else:
#     print('number is first')
        
