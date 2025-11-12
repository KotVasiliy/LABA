import math
from time import *

def ugol():
    X = 4.5  # длина палки
    Y = 2.0
    while Y <= 3.0:
        # Угол находим через арккосинус: cos(a) = Y/X
        ugol_rad = math.acos(Y / X)
        ugol_deg = math.degrees(ugol_rad)
        print(f"Расстояние Y: {Y:.1f} м\tУгол (рад): {ugol_rad:.4f}\tУгол (град): {ugol_deg:.2f}°")
        Y += 0.2


print("Задание 1:")
ugol()

print("-"*100)
print("Задание 2:")

def ERROR_x0_bigger_then_x1():
    sleep(1)
    print(f"ERROR_x0_bigger_then_x1\tВВЕДЁН НЕВЕРНЫЙ ЧИСЛОВОЙ ОТРЕЗОК\tERROR_x0_bigger_then_x1\tВВЕДЁН НЕВЕРНЫЙ ЧИСЛОВОЙ ОТРЕЗОК")
    sleep(1)
    print("НАХОДИМ РЕШЕНИЕ ВАШЕЙ ПРОБЛЕМЫ")
    sleep(0.1)
    print("　∧＿∧")
    sleep(1)
    print("（｡･ω･｡)つ━☆・*。")
    sleep(1)
    print("⊂　　 ノ 　　　・゜+.")
    sleep(1)
    print("しーＪ　　　°。+ *´¨)")
    sleep(1)
    print("　　　　　　　　.• ´¸.•*´¨) ¸.•*¨)")
    sleep(1)
    print("　　　　　　　　　(¸.•´ (¸.•’*")
    sleep(1)
    print("ЗНАЧЕНИЕ X0 БОЛЬШЕ ЗНАЧЕНИЯ X1\nВВЕДИТЕ КОРРЕКТНЫЕ ЗНАЧЕНИЯ, ГДЕ X0 < X1")
    ex_2()



def ERROR_negative_or_zero_step():
    sleep(1)
    print(
        f"ERROR_negative_step\tВВЕДЁН НЕВЕРНЫЙ ШАГ\tERROR_negative_step\tВВЕДЁН НЕВЕРНЫЙ ШАГ")
    sleep(1)
    print("НАХОДИМ РЕШЕНИЕ ВАШЕЙ ПРОБЛЕМЫ")
    sleep(0.1)
    print("　∧＿∧")
    sleep(1)
    print("（｡･ω･｡)つ━☆・*。")
    sleep(1)
    print("⊂　　 ノ 　　　・゜+.")
    sleep(1)
    print("しーＪ　　　°。+ *´¨)")
    sleep(1)
    print("　　　　　　　　.• ´¸.•*´¨) ¸.•*¨)")
    sleep(1)
    print("　　　　　　　　　(¸.•´ (¸.•’*")
    sleep(1)
    print("ШАГ ЯВЛЯЕТСЯ ОТРИЦАТЕЛЬНЫМ ЧИСЛОМ ИЛИ РАВЕН НУЛЮ, ЧТО НЕДОПУСТИМО ДЛЯ ОТРЕЗКА [X0;X1]\nВВЕДИТЕ КОРРЕКТНОЕ ЗНАЧЕНИЕ ШАГА")
    ex_2()



def ex_2():
    # Ввод данных
    X0 = float(input("Введите начальное значение X0: "))
    X1 = float(input("Введите конечное значение X1: "))
    if X0 > X1:
        ERROR_x0_bigger_then_x1()
    dX = float(input("Введите шаг dX: "))
    if dX <= 0:
        ERROR_negative_or_zero_step()


    x = X0
    while x <= X1:
        if x < 0:
            z = x ** 2
        elif 0 <= x <= 1:
            z = math.sin(x)
        else:
            z = math.cos(x)
        print(f"X: {x:.2f}\t Z: {z:.4f}")
        x += dX

ex_2()

