import random as rn
choices=['r' , 'p','s']
randomChoices=rn.randint(0,len(choices)-1)
cumputer=choices[randomChoices]


try:
    def rps(urChoice):
        if urChoice=='r' and cumputer=='s':
            return f'i got {cumputer} ouch that hurt ok u won'
        elif urChoice=='r' and cumputer=='p':
            return f'i got{cumputer} haha got ya u cant see anythin can u?? '
        elif urChoice==cumputer:
            return f'i got {cumputer} aight tie'
        elif urChoice=='p' and cumputer=='r':
            return f"i got {cumputer} ahhh wait i cant see anythin"
        elif urChoice=='p' and cumputer=='s':
            return f"i got {cumputer} aigh ima intdivision u now"
        elif urChoice=='s' and cumputer=='r':
            return f'i got {cumputer} ima smash u now'
        else:
            return 'oh wait plz have mercy'
         
except:
    print('sorry this happened make sure that ur input is correct and its not a number or anything else than [r,p and]!!!')



print(rps())
