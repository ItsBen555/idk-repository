def multi(a,b):
    divis=0
    divis+=1
    if a==divis:
        return a

    return a-multi(b,a+1)
    
  
print(multi(15,5))

# a=15,b=3
# 15-5 ---->>>10 b=2 
# 10-5------->5 b=1
# 5------>0 b=0