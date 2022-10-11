def discounted(price, discount, max_discount = 20) :
    try :
        price = float(abs(price))
        discount = float(abs(discount))
        max_discount = int(abs(max_discount))
    except (ValueError, TypeError) :
        return "Введены не оч данные, го еще"

    if max_discount > 100 :
        raise ValueError('Максимальная скидка не должна быть больше 100')
    if discount > max_discount : 
        price_with_discount = price
    else :
        price_with_discount = price - (price * discount / 100)
    return (price_with_discount)

if __name__ == "__main__" :
    print(discounted(90,-14))
    print(discounted(16666,18))
    print(discounted(90,109))
    print(discounted(90,'14'))
    print(discounted(90,14))