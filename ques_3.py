a = [4, 2, 1, 2, 2, 3, 4, 4, 4]
dict= {}
for i in a:
    dict[i] = dict.get(i, 0) + 1

min_frequency = None
min_frequency_num = None

for a, j in dict.items():
    if min_frequency is None or j < min_frequency:
        min_frequency = j
        min_frequency_num = a

print("The element with the minimum frequency is:", min_frequency_num)
