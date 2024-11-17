users_time = int(input('Введите время от 0 до 23: '))

# Проверка корректности ввода
if users_time < 0 or users_time > 23:
    print("Ошибка! Время должно быть от 0 до 23 часов")
else:
    if 4 <= users_time <= 11:
        print("Доброе утро!")
    elif 11 < users_time <= 17:
        print("Добрый день!")
    elif 17 < users_time <= 22:
        print("Добрый вечер!")
    else:
        print("Доброй ночи!")