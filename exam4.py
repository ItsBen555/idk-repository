scoreNumber=int(input('please enter your tally marks so i can transform them into an score :'))

if scoreNumber<10 and scoreNumber>=0:
    print(f'{scoreNumber} = F')

elif 9<=scoreNumber<14 :   
   print(f"{scoreNumber} = C")

elif 14<=scoreNumber<17:
    print(f'{scoreNumber} = B')


elif 17<=scoreNumber<21:
    print(f'{scoreNumber} = A')

else:
    print('number is bigger than 20 or less than 0')


                



