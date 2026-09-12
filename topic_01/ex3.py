def discriminant():
    a = float(input("Введіть a:"))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    d = pow(b, 2) - 4 * a * c
    if d < 0:
        print("Рівняння не має розв'язків. Дискримінант:", d)
    elif d == 0:
        print("Рівняння має 1 корінь. Дискримінант:", d)
    else:
        print("Дискримінант:", d)

discriminant()