import random

list = [random.randint(1,20) for i in range(10)]

print(list)

n = len(list)

for i in range(1,n):
    key = list[i]
    j = i - 1
    while j >= 0 and list[j]>key:
        list[j+1] = list[j]
        j = j-1
        print(list)
    list[j+1] = key

print(list)