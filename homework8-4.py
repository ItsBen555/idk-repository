people = ["mojtaba", "mojtaba", "taghi", "naghi", "sakineh", "sara", "mojtaba", "mojtaba", "mojtaba", "mojtaba", "mojtaba"]
people2=[]


for i in people:
    if i not in people2:
        people2.append(i)
        

print(people2)


# def count_cases(string):
#     # string==str

#     lowercase=0 #the lowercase is equal to 0 at the start
#     uppercase=0 #so is the uppercase

#     for i in string:
#         # if i=="":
#         #     pass #cuz the for statement counts the space in the string as well

#         if i.islower():
#             lowercase+=1
#         else:

#             uppercase+=1

#         return(f"the lower case is equal to {lowercase}"),(f"and the upper case is equal to {uppercase}")


# print(count_cases('Hello My name IS Benyamin'))