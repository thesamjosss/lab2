# Зчитування 5 цілих чисел
numbers = [int(input()) for _ in range(5)]

# Розрахунок елементів, які більші за 0
positive_count = sum(1 for x in numbers if x > 0)

# Вивід результату
print(positive_count)


