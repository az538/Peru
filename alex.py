import random

value2 = 0
value = 0
list = []
ellements = input("how many ellements ")

for x in range(0, int(ellements)):
    list.append(random.randint(1, 101))
print("Original :" + str(list))

for outer in range(0, int(ellements)):
    for x in range(0, int(ellements)):
        if (x + 1) < int(ellements) and list[x] < list[x + 1]:
            value = list[x]
            value2 = list[x + 1]
            print(
                str(x) + " " + str(x + 1) + " values: " + str(value) + " " + str(value2)
            )
            list[x] = value2
            list[x + 1] = value
        print(list)
