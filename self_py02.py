users_time = int(input('Введите время от 0 до 23: '))

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

# Создайте программу для определения стоимости доставки заказа:
# - Запросить у пользователя:
#   * расстояние доставки (в км)
#   * вес заказа (в кг)
#   * является ли клиент постоянным (да/нет)
# - Рассчитать стоимость доставки по правилам:
#   * Базовая стоимость - 200 рублей
#   * За каждый километр после 3-х +50 рублей
#   * За каждый кг после 10-ти +70 рублей
#   * Постоянным клиентам скидка 10%
# - Вывести итоговую стоимость с пояснением расчёта

distance = float(input('Введите расстояние доставки в км: '))
weight = float(input('Введите вес заказа в кг: '))
is_regular_client = str(input('Вы постоянный клиент (да/нет): '))
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

if is_regular_client.lower() == 'да' or is_regular_client.lower() == 'y':
    delivery_cost = delivery_cost * 0.9
else:
    delivery_cost * 1

print(f'''
Расчёт стоимости доставки:
Базовая стоимость: {base_cost} руб.
Надбавка за расстояние: {round((extra_distance * 50), 2)} руб.
Надбавка за вес: {round((extra_weight * 70), 2)} руб.
{'Скидка постоянного клиента 10%' if is_regular_client.lower() == 'да' or is_regular_client.lower() == 'y' else 'Скидка не применяется'}
Итоговая стоимость: {round(delivery_cost, 2)} руб.
''')


