
def caps_counter(sentence):
    #sentence=str

    lowercase=0 #the lowercase vari is 0 at first
    uppercase=0 #so is the uppercase

    for i in sentence:
      
        if i==" ":
            continue #cuz the for statement counts the space as well

        if i.islower():
            lowercase+=1 #add 1 to the previous lowercase so if it was 2 it will be 3

        else: #if it wasnt our if statement
            uppercase+=1 #do the same process with uppercase
    return(lowercase,uppercase)

print(caps_counter("hello my Name Is Benyamin"))




