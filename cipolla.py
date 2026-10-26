import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def legendre_symbol(a, p):
    res = pow(a, (p - 1) // 2, p)
    return -1 if res == p - 1 else res


def poly_mul(P, Q, b, a, p):
    # P = p0 + p1*y, Q = q0 + q1*y
    p0, p1 = P
    q0, q1 = Q

    # P*Q = (p0*q0) + (p0*q1 + p1*q0)*y + (p1*q1)*y^2
    r0 = (p0 * q0) % p
    r1 = (p0 * q1 + p1 * q0) % p
    r2 = (p1 * q1) % p

    # так как y^2 == by - a (mod f(y)), заменяем y^2:
    # r2 * y^2 = r2 * (b*y - a) = (-r2*a) + (r2*b)*y
    r0 = (r0 - r2 * a) % p
    r1 = (r1 + r2 * b) % p

    return (r0, r1)


def poly_pow(base, exp, b, a, p):
    res = (1, 0)
    while exp > 0:
        if exp % 2 == 1:
            res = poly_mul(res, base, b, a, p)
        base = poly_mul(base, base, b, a, p)
        exp //= 2
    return res


def cipolla(a, p):
    if not is_prime(p):
       raise ValueError(f"Ошибка: число p не является простым числом")

    if a < 0:
        raise ValueError(f"Ошибка: число a не является натуральным")
    a = a % p
    if a == 0:
        return 0, 0

    if legendre_symbol(a, p) != 1:
        return None

    while True:
        b = random.randint(0, p - 1)
        discriminant = (b ** 2 - 4 * a) % p
        if legendre_symbol(discriminant, p) == -1:
            break

    # положить f(y) = y^2 - by + a
    # найти x0 как остаток от деления y^((p + 1) / 2) на f(y)
    # многочлен 'y' записывается как (0, 1), то есть 0 + 1*y
    poly_y = (0, 1)
    power_exp = (p + 1) // 2

    remainder = poly_pow(poly_y, power_exp, b, a, p)

    x0 = remainder[0]
    x1 = (p - x0) % p

    return sorted([x0, x1])
