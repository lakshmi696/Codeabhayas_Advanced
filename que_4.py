a=[40,50,10,20,30]
second_largest=a[0]
largest=a[0]
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
for i in range(len(a)):
    if a[i]>second_largest and a[i]!=largest:
        second_largest=a[i]
print("second largest",second_largest)
    
