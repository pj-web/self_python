user_height = float(input("Введите ваш рост: "))
user_weight = float(input("Введите ваш вес: "))

body_mass_index = user_weight / (user_height * user_height)

print(f'Ваш индекс массы тела равен: {round(body_mass_index, 2)}')
