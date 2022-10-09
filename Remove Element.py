thislist = [0,1,2,2,3,0,4,2]
for item in thislist[:]:
    print(item)
    if item == 2:
        thislist.remove(item)

print(thislist)        