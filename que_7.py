a = [1, 3, 5, 7, 9,1]
flag = 1
n = len(a)
for i in range(1, n):
    if a[i] < a[i - 1]:
        flag = 0
        break
if flag==1:
    print("The array is sorted.")
else:
    print("The array is not sorted.")
