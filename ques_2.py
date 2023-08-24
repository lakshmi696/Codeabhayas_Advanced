a=[1,1,1,2,3,3,4,5,5,6]
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
max_freq=0
number=None
for a,j in dict.items():
    if j>max_freq:
        max_freq=j
        j=a
print(j)
    
        
