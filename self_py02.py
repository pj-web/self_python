users_time = int(input('Введите время от 0 до 23: '))


if 4 < users_time < 11:
    print("Доброе утро!")
elif 11 < users_time < 17:
    print("Добрый день!")
elif 17 < users_time < 22:
    print("Добрый вечер!")
els

# - Запрашивать у пользователя текущий час (от 0 до 23)
# - Выводить приветствие в зависимости от времени:
#   * с 4 до 11 - "Доброе утро!"
#   * с 11 до 17 - "Добрый день!"
#   * с 17 до 22 - "Добрый вечер!"
#   * с 22 до 4 - "Доброй ночи!"