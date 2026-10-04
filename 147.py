# Зчитуємо першу точку і радіус
x1 = float(input())
y1 = float(input())
r1 = float(input())

# Зчитуємо другу точку і радіус
x2 = float(input())
y2 = float(input())
r2 = float(input())

# Перевірка першої точки
if x1**2 + y1**2 <= r1**2:
    print("The point belongs to the circle")
else:
    print("The point is outside the circle")

# Перевірка другої точки
if x2**2 + y2**2 <= r2**2:
    print("The point belongs to the circle")
else:
    print("The point is outside the circle")

