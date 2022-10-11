""" while True:  #Способ сделать бесконечный цикл   # Из while задача
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break  #Здесь цикл надо закончить
    else:
        print('Сам ты {}'.format(user_say)) """


def hello_user() :
    while True :
        try :
            user_say = input('Скажи как дела: ').capitalize() # Первая буква заглавная
            if user_say == 'Хорошо' :
                print('Ну оке')
                break
        except KeyboardInterrupt :
            print('Пока')
            break

if __name__ == "__main__" :
    hello_user()