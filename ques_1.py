a=[1,1,1,2,3,3,4,5,5,6]
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
