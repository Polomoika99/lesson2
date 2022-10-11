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


new_price = discounted(100000, 10, phone_name = 'Iphone12')
print(new_price)  #100 000 - после изменения функции должно быть так

new_price = discounted(40000, 20, phone_name = 'Samsung')
print(new_price)  #32 000

new_price = discounted(5000, 20)
print(new_price)  #4 000





#balance = 100
#price = 50
#in_stock = 10  # Товар в наличии


# print(bool(balance > price))  #Проверка на True/False, операция по сути как условный оператор
# print(bool(in_stock))  

# if balance > price and in_stock:
#     print('Одобряем оплату покупки')
# elif not in_stock :
#     print("Товара нет в наличии")
# else:
#     print('Пожалуйста, пополните баланс!')





#def check_weather(temperature):
#    if temperature < 0 :
#        return "На улице холодно"
#    elif temperature >= 0 and temperature < 15 :
#        return "На улице прохладно"
#    elif temperature >= 15 and temperature < 25 :
#        return "На улице тепло"
#    elif temperature >= 25 :
#        return "На улице жарко"
#    return 'Не работает'


#print(check_weather(-2))  # "На улице холодно"
#print(check_weather(8))  # "На улице прохладно"
#print(check_weather(20))  # "На улице тепло"
#print(check_weather(30))  # "На улице жарко"