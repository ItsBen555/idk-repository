colors = ["red", "blue", "crimson", "blue", "green", "crimson", "crimson", "purple", "blue", "blue", "pink", "white", "pink", "pink"]
colors2=[]
for i in colors:
    if i not in colors2:
        colors2.append(i)
print(colors2)

# input:colors = ["red", "blue", "crimson", "blue", "green", "crimson", "crimson", "purple", "blue", "blue", "pink", "white", "pink", "pink"]

# output= ['red','blue','crimson , 'green' ,'purple' ,'pink,'white']