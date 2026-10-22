import random

#list = [random.randint(1, 20) for i in range(10)]
list = [15,14,10,4,2]

print(list)

n = len(list)
swap = False
count = 0
c = 0
for i in range(n):
    swap = False
    for j in range(n - i - 1):
        c = c+1
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            swap = True
            count = count + 1
            print(list)
    #if not swap:
    #    break
print(swap)
print(count)
print(list)
print(c)