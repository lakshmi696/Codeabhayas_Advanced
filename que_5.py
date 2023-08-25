a=[1,2,2,1,2,3,4,5,5,3,4]
b=[]
for i in a:
    if i not in b:
        b+=[i]
print("Array without duplicates",b)
