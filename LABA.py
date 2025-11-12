import math

def ugol():
    X = 4.5  # длина палки
    Y = 2.0
    while Y <= 3.0:
        # Угол находим через арккосинус: cos(a) = Y/X
        ugol_rad = math.acos(Y / X)
        ugol_deg = math.degrees(ugol_rad)
        print(f"Расстояние Y: {Y:.1f} м\tУгол (рад): {ugol_rad:.4f}\tУгол (град): {ugol_deg:.2f}°")
        Y += 0.2

# Вызываем функцию
print("Задание 1:")
ugol()