import random

xo_symbols = ('X', '0')  # - символы для игры

xo_field = [' '] * 9  # - список для хранения содержимого игрового поля

win_moves = [  # - номера заполненных ячеек для победы
    [1, 2, 3],  # - 1 строка
    [4, 5, 6],  # - 2 строка
    [7, 8, 9],  # - 3 строка
    [1, 4, 7],  # - 1 столбец
    [2, 5, 8],  # - 2 столбец
    [3, 6, 9],  # - 3 столбец
    [1, 5, 9],  # - главная диагональ
    [3, 5, 7]  # - второстепенная диагональ
]


# - функция вывода игрового поля
def print_field(list_):
    print('Номера ячеек:' + ' ' * 5 + 'Игровое поле:')
    print('1\u25032\u25033' + ' ' * 15 + f'{list_[0]}\u2503{list_[1]}\u2503{list_[2]}')
    print('\u2501\u254b\u2501\u254b\u2501' + ' ' * 15 + '\u2501\u254b\u2501\u254b\u2501')
    print('4\u25035\u25036' + ' ' * 15 + f'{list_[3]}\u2503{list_[4]}\u2503{list_[5]}')
    print('\u2501\u254b\u2501\u254b\u2501' + ' ' * 15 + '\u2501\u254b\u2501\u254b\u2501')
    print('7\u25038\u25039' + ' ' * 15 + f'{list_[6]}\u2503{list_[7]}\u2503{list_[8]}')


def check_win(list_, c):  # - проверка победы игрока, который ходил символом 'c'
    def check_variant(v, c_):
        return list_[v[0] - 1] == list_[v[1] - 1] == list_[v[2] - 1] == c_

    return any([check_variant(x, c) for x in win_moves])


def player_move(number_player):  # - ход игрока
    cell_number = -1
    while cell_number < 0:  # - повторяем пока не будет введено корректное для нас значение
        print_field(xo_field)  # - вывод игрового поля
        print(f'Ход {number_player + 1}-го игрока ("{xo_symbols[number_player]}").')
        try:  # - обработка "неправильных" символов
            cell_number = int(input('Введите номер ячейки для хода (0 - для выхода из игры): '))
            if xo_field[cell_number - 1] != ' ':
                print('Выбранная ячейка уже занята!')
                cell_number = -1
        except:
            cell_number = -1
            print('Недопустимое значение! Ход не засчитан, повторите.')
    return cell_number


def bot_move(num_player_bot):  # - ход противника-компьютера символом с номером num_player_bot

    # - Правило 1. Если игрок может немедленно выиграть, он это делает
    # - Правило 2. Если игрок не может немедленно выиграть, но его противник мог бы немедленно выиграть,
    #   сделав ход в какую-то клетку, игрок сам делает ход в эту клетку, предотвращая немедленный проигрыш

    # - передав в n номер бота проверяем правило 1, передав номер игрока - проверяем правило 2
    def check_rule(n):
        right_cell = 0
        field_copy = xo_field.copy()
        for i in range(1, 9):
            if field_copy[i - 1] == ' ':
                field_copy[i - 1] = xo_symbols[n]
                if check_win(field_copy, xo_symbols[n]):
                    right_cell = i
                    break
                else:
                    field_copy[i - 1] = ' '
        return right_cell

    cell = check_rule(num_player_bot)  # - проверка правила 1
    if cell:
        return cell

    cell = check_rule((num_player_bot + 1) % 2)  # - проверка правила 2
    if cell:
        return cell

    # - если ход по правилам не найден - выбираем произвольную ячейку для хода
    while True:
        cell = random.randint(1, 9)
        if xo_field[cell - 1] == ' ':
            return cell


def game(game_type):
    bot = -1
    if game_type == 2:
        bot = random.randint(1, 100) % 2  # - определяем случайно, кто будет ходить первым - компьютер или
        # игрок
        if bot:
            print('Игрок ходит первым!')
        else:
            print('Компьютер ходит первым!')

    k = 0  # - номер хода
    while True:
        if (game_type == 2) and (k % 2 == bot):
            cell = bot_move(bot)  # - ход компьютера
        else:
            cell = player_move(k % 2)  # - ход игрока
        if cell:
            xo_field[cell - 1] = xo_symbols[k % 2]  # - сохранение символа в игровое поле
        else:
            print('Игра завершена досрочно.')
            return False  # - завершаем игру
        if check_win(xo_field, xo_symbols[k % 2]):  # - проверка победы на данном ходе
            print_field(xo_field)
            if (game_type == 2) and (k % 2 == bot):
                print('Компьютер победил!')
            else:
                print(f'Игрок {k % 2 + 1} победил!')
            break
        k += 1
        if k == 9:  # - если ходы закончились - ничья
            print_field(xo_field)
            print('Ничья! Игра завершена.')
            break

    # - возможность повторной игры
    answer = input('Желаете повторить? Введите y или Y для повторной игры: ')
    return answer == 'y' or answer == 'Y'


if __name__ == '__main__':
    print('Игра "Крестики-нолики".')
    print(' --- 1. Игрок против игрока.')
    print(' --- 2. Игрок против компьютера.')
    print(' --- 0. Выход.')

    game_type = -1
    while game_type not in {0, 1, 2}:  # - выбор режима игры
        try:
            game_type = int(input('Введите режим игры (0 - для выхода): '))
        except:
            game_type = -1

    if game_type:
        while game(game_type):  # - запускаем игру выбранного типа
            xo_field = [' '] * 9  # - очищаем игровое поле
    else:
        print('Игра завершена.')
