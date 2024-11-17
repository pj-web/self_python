# Функция для получения числового ввода с проверкой
def get_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка! Значение должно быть положительным числом")
                continue
            return value
        except ValueError:
            print("Ошибка! Пожалуйста, введите число")

# Функция для получения ответа да/нет
def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ['да', 'нет', 'y', 'n', 'yes', 'no']:
            return answer
        print("Ошибка! Ответьте 'да' или 'нет'")


# Основная программа
# Получаем данные с помощью наших функций
distance = get_number_input('Введите расстояние доставки в км: ')
weight = get_number_input('Введите вес заказа в кг: ')
is_regular_client = get_yes_no_input('Вы постоянный клиент (да/нет): ')

# Расчёт стоимости
base_cost = 200

if distance > 3:
    extra_distance = distance - 3
else:
    extra_distance = 0

if weight > 10:
    extra_weight = weight - 10
else:
    extra_weight = 0

delivery_cost = base_cost + (extra_distance * 50) + (extra_weight * 70)

# Применение скидки
if is_regular_client in ['да', 'y', 'yes']:
    delivery_cost = delivery_cost * 0.9

# Вывод результата
print(f'''
Расчёт стоимости доставки:
Базовая стоимость: {base_cost} руб.
Надбавка за расстояние: {extra_distance * 50} руб.
Надбавка за вес: {extra_weight * 70} руб.
{'Скидка постоянного клиента 10%' if is_regular_client in ['да', 'y', 'yes'] else 'Скидка не применяется'}
Итоговая стоимость: {round(delivery_cost, 2)} руб.
''')