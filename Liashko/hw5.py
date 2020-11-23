import string

shfr = input('Вы хотите зашифровать(Z) либо расшифровать(R)').upper()


def cezar_shifr(lines_file):
    shifr = []
    for i in range(len(lines_file[0])):
        # проверка буква ли это
        if lines_file[0][i].isalpha():
            # проверка большая буква или маленькая
            if lines_file[0][i].isupper():
                abc = string.ascii_uppercase
            else:
                abc = string.ascii_lowercase
            j = abc.find(lines_file[0][i])
            k = j + int(key_z)
            # проверка или не выходит за кол-во букв в алфавите
            if k >= len(string.ascii_lowercase):
                g = abc[k - len(string.ascii_lowercase)]
            else:
                g = abc[k]
        else:
            g = lines_file[0][i]
        shifr.append(g)
    shifrs = ''.join(shifr)
    return shifrs


while True:
    try:
        if shfr == 'Z':
            try:
                name_file = input('Введите имя файла для его зашифровки')
                with open(name_file + '.txt') as file:
                    lines_file = file.readlines()
            except FileNotFoundError:
                print('Ошибка: Просьба ввести существующий файл для шифровки')
                break
            name_file_z = input('Введите имя зафрованного файла')
            key_z = int(input('Ключ сдвига'))
            with open(name_file_z + '.txt', 'w+') as file:
                file.write(cezar_shifr(lines_file))
        elif shfr == 'R':
            try:
                name_file_roz = input('Введите имя файла для расшифровки')
                with open(name_file_roz + '.txt') as file:
                    lines_file = file.readlines()
            except FileNotFoundError:
                print('Ошибка: Просьба ввести существующий файл для шифровки')
                break
            name_file_a = input('Введите имя файла после его расшифровки')
            key_z = int(input('Ключ сдвига'))
            # изменение для дешифратора
            key_z = - key_z
            with open(name_file_a + '.txt', 'w+') as file:
                file.write(cezar_shifr(lines_file))
        else:
            print('Ошибка: Введите верное значение')
            break
    except ValueError:
        print('Ошибка: Просьба ввести цифру')
        break
    break
