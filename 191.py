# Зчитування розмірів цеглини й отвору
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# Сортування 3 сторони цеглини та 2 сторони отвору по збільшенню
brick = sorted([a, b, c])
hole = sorted([d, e])

# Порівняння двох найменших сторони цеглини з двома сторонами отвору
if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print("Yes")
else:
    print("No")


