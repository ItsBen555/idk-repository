listOne=["black",'gray','yellow',True,False]
listsecend=[]
import random as rn

def randomlist(list):
    rn.shuffle(list)


    for i in list:
        if i not in listsecend:
            listsecend.append(i)
    return listsecend

print(randomlist([1,2,3,4,5,6,]))
    