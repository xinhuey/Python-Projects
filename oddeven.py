from array import array
evnum = array("i")
oddnum = array("i")
for x in range(20,40):
    if x%2 == 0:
        evnum.append(x)
        
    else:
        oddnum.append(x)
print("Even number: ",end="")
for cnt in range (0, len(evnum)):
    print(evnum[cnt], end=",")
print(" ")
print("Odd number: ", end="")
for cnt in range(0, len(oddnum)):
    print(oddnum[cnt], end=",")
