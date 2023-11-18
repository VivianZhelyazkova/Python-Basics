from math import pi
area = 0
type_of_the_figure = input()
if type_of_the_figure == "square":
    side = float(input())
    area = side * side



elif type_of_the_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b



elif type_of_the_figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)


elif type_of_the_figure == "triangle":
    length = float(input())
    hight = float(input())
    area = (length * hight) / 2

print(f"{area:.3f}")


