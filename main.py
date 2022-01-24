xo_symbols = ('X', '0')     # - символы для игры

xo_field = [' '] * 9        # - список для хранения содержимого игрового поля

win_moves = [       # - номера заполненных ячеек для победы
    [1, 2, 3],      # - 1 строка
    [4, 5, 6],      # - 2 строка
    [7, 8, 9],      # - 3 строка
    [1, 4, 7],      # - 1 столбец
    [2, 5, 8],      # - 2 столбец
    [3, 6, 9],      # - 3 столбец
    [1, 5, 9],      # - главная диагональ
    [3, 5, 7]       # - второстепенная диагональ
]


# - функция вывода игрового поля
def print_field(list_):
    print('Номера ячеек:' + ' ' * 5 + 'Игровое поле:')
    print('1\u25032\u25033' + ' ' * 15 + f'{list_[0]}\u2503{list_[1]}\u2503{list_[2]}')
    print('\u2501\u254b\u2501\u254b\u2501' + ' ' * 15 + '\u2501\u254b\u2501\u254b\u2501')
    print('4\u25035\u25036' + ' ' * 15 + f'{list_[3]}\u2503{list_[4]}\u2503{list_[5]}')
    print('\u2501\u254b\u2501\u254b\u2501' + ' ' * 15 + '\u2501\u254b\u2501\u254b\u2501')
    print('7\u25038\u25039' + ' ' * 15 + f'{list_[6]}\u2503{list_[7]}\u2503{list_[8]}')


def check_win(list_, c):        # - проверка победы игрока, который ходил символом 'c'
    def check_variant(v, c_):
        return list_[v[0]-1] == list_[v[1]-1] == list_[v[2]-1] == c_
    return any([check_variant(x, c) for x in win_moves])


def player_move(number_player):
    cell_number = -1
    while cell_number < 0:
        print_field(xo_field)
        print(f'Ход {number_player + 1}-го игрока ("{xo_symbols[number_player]}").')
        try:
            cell_number = int(input('Введите номер ячейки для хода (0 - для выхода из игры): '))
            if xo_field[cell_number-1] != ' ':
                print('Выбранная ячейка уже занята!')
                cell_number = -1
        except:
            cell_number = -1
            print('Недопустимое значение! Ход не засчитан, повторите.')
    return cell_number



def game():
    k = 0              # - номер хода
    while True:
        cell = player_move(k % 2)
        if cell:
            xo_field[cell-1] = xo_symbols[k % 2]
        else:
            print('Игра завершена досрочно.')
            break
        if check_win(xo_field, xo_symbols[k % 2]):
            print_field(xo_field)
            print(f'Игрок {k % 2 + 1} победил!')
            break
        k += 1
        if k == 9:
            print_field(xo_field)
            print('Ничья! Игра завершена.')
            break

if __name__ == '__main__':
    print('Игра "Крестики-нолики".')
    game()
