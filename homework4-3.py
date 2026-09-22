input = [1, [2, 3, [4, 5, 6], 7, 8], 9]
output=[]

sumt=0
for i in input:
    if type(i)==int:
        output.append(i)
    else:
        for j in i:
            if type(j)==int:
                output.append(j)
            else:
                for z in j:
                    if type(z)==int:
                        output.append(z)

print(output)

    
        