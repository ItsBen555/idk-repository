# num1=int(input('please enter the first number : ')) #4
# num2=int(input('please enter the secend number : ')) #8
# num3=int(input('please enter the last number : ')) #5
# maximum=num3

# #maximum=5

# if num2>maximum: #8>5
#     maximum=num2

#     #maximum=8
# if num1>maximum: #4<8
#     maximum=num1

# print(f'maximum = {maximum}') #maximum=8
num1=int(input('please enter the first number : ')) #4
maximum=num1
for i in range(0,2):
    num=int(input('please enter number :'))
    if num>maximum:
        maximum=num
print(f"the maximum number = {maximum}")


