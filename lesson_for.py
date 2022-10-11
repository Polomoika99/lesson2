for number in range(3) :
    print(f'Номер {number}') #Будет (все в столбец) Номер 0, Номер 1, Номер 2




for letter in 'python':
    print(letter.upper())  # Будет (в столбец) P Y T H O N 




my_string = 'Привет, я учу python'

for word in my_string.split():
    print(f'Длина слова {word} : {len(word)}') # Будет (все в столбец) Длина слова Привет, : 7, Длина слова я : 1, Длина слова учу : 3, Длина слова python : 6





students_scores = [3, 5, 4, 4, 2]

avg_score = 0
for score in students_scores :
    print('До', avg_score)
    avg_score = avg_score + score
    print('После', avg_score)

class_avg = avg_score  / len(students_scores) #Средняя оценка по классу
print(f'Средняя оценка {class_avg}')  # Средняя оценка 3.6







stock = [
		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
                'discount': 25},
		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
                'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

def discounted(price, discount, max_discount = 30, phone_name = ''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name : 
        return price
    else:
        return price - (price * discount / 100)

for phone in stock :
    phone['price_final'] = discounted(
        phone['price'], 
        phone['discount'], 
        phone_name=phone['name'] # Можно все в одну строку написать, а можно и так
    ) #По всем трем телефонам финальная цена (айфон и ноунейм цена не меняется по условию)

print(stock)







classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]

def count_class_avg(students_scores1) :  #Функция принимает оценки студента
    scores_sum = 0
    for score in students_scores1 :  # Перебираем по одной оценке и прибавляем
        scores_sum += score
    return scores_sum / len(students_scores1)

school_avg_sum = 0
for one_class in classes :
    class_avg = count_class_avg(one_class['scores'])
    print(f'Средняя оценка класса {one_class["name"]} : {class_avg}') # Будет (в столбец) Средняя оценка класса 3А : 3.6, Средняя оценка класса 3Б : 3.4, Средняя оценка класса 3В : 4.2
    school_avg_sum += class_avg

school_avg = round(school_avg_sum / len(classes), 2) # Округление до двух знаков
print(f'Средняя оценка по школе : {school_avg}') # Будет Средняя оценка по школе : 3.73