def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def koreni(a, b, c):

    d = discriminant(a, b, c)
    print("Дискримінант D =", d)

    if d < 0:
        print("Рівняння не має дійсних коренів.")
    elif d == 0:
        x = -b / (2 * a)
        print("Рівняння має один корінь: x =", x)
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        print("Рівняння має два корені: x1 =", x1, "x2 =", x2)


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

koreni(a, b, c)