while True:  #Способ сделать бесконечный цикл
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break  #Здесь цикл надо закончить
    else:
        print('Сам ты {}'.format(user_say))