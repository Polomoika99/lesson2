# import random

def cut_cake(people):
    try :
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except ZeroDivisionError:  # Исключение ввели, на 0 делить нельзя
        print('Не надо делить на 0!')
    except TypeError : # На строку делить нельзя (int/str)
        print('На строку не дели, брат.')

cut_cake(4) # Еще можно писать исключения в строку except(ZeroDivisionError, TypeError):


# while True:
#     P = random.randint(1, 10)
#     cut_cake(P)