#   =======№1=======
#from datetime import datetime

#def get_days_from_today(date:str) -> int:
#    try:
 #       return (datetime.strptime(date, "%Y-%m-%d").date() - datetime.now().date()).days
#    except ValueError:
#        return ('Некоректний формат вводу !!!')
#a = input("Введіть дату: ")
#print(get_days_from_today(a))



#   =======№2=======
import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка коректності вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= (max_num - min_num + 1)):
        return []  # Повертаємо пустий список, якщо параметри не відповідають вимогам

    # Генеруємо список унікальних випадкових чисел
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers.sort()  # Сортуємо числа в порядку зростання
    return numbers

min_zahlen, max_zahlen, count_zahlen = int(input('Введіть мінімальне число: ')), int(input('Введіть максимальне число: ')), int(input('Введіть кількість чисел у вибірці: '))
lottery_numbers = get_numbers_ticket(min_zahlen, max_zahlen, count_zahlen)

print("Ваші лотерейні числа:", lottery_numbers)

#   =======№3=======
#import re


#def normalize_phone(phone_number):
 #   formatted_phone = []

 #   pattern = r"[;,\-:!\.()+\\t n]"
 #   replacement = r""
 #   formatted_phone = ('+' + '38' + re.sub(pattern, replacement, phone_number)[-10:])
 #   return formatted_phone10



#phone = input('Введіть номер для корекції: ')

#print(normalize_phone(phone))

#phone = [
#    "067\\t123 4567",
#    "(095) 234-5678\\n",
#    "+380 44 123 4567",
#    "380501234567",
#    "    +38(050)123-32-34",
#    "     0503451234",
#    "(050)8889900",
#    "38050-111-22-22",
#    "38050 111 22 11   ",
#]