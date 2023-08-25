a= [1, 2, 3, 4, 5]
n = len(a)
last_element = a[-1]

for i in range(n - 1, 0, -1):
    a[i] = a[i - 1]

a[0] = last_element

print("Array after right rotation:", a)
