plaing = list(range(1, 10))


def func():
    for i in range(3):
        print(plaing[0 + i * 3], plaing[1 + i * 3], plaing[2 + i * 3])


def input_(play):
    while True:
        value = input('Где будет стоять знак: ' + play)
        if not value in '123456789':
            print('Ошибочный ввод')
            continue
        value = int(value)
        if str(plaing[value - 1]) in 'XO':
            print('Эта клетка занята')
            continue
        plaing[value - 1] = play
        break


def main():
    counter = 0
    while True:
        func()
        if counter % 2 == 0:
            input_('X')
        else:
            input_('O')
        counter += 1


main()
