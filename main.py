from cipolla import cipolla

def console_interface():
    while True:
        print("\nРешение сравнения вида x^2=a(mod p).\n")
        user_input_a = input("Введите натуральное число 'a': ").strip()
        user_input_p = input("Введите нечетное простое число 'p': ").strip()
        try:
            a = int(user_input_a)
            p = int(user_input_p)
        except ValueError:
            print("\nВводите только целые числа.\n")
            continue

        try:
            roots = cipolla(a, p)
            print(f"Корни уравнения x^2 ≡ {a} (mod {p}): {roots}")
            if roots is not None:
                print(f"Проверка: {roots[0] ** 2 % p} = {roots[1] ** 2 % p} = {a}")
        except ValueError as e:
            print(f"{e}\n")
            continue

if __name__ == "__main__":
    console_interface()