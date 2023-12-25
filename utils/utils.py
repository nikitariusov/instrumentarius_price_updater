import easygui


def only_integer(price):
    i = price.find('.')
    if i < 0:
        return price
    else:
        return price[:i]


def open_file(file_name=''):
    """открытие файла"""
    print(f'Выбери {file_name} файл:\n')
    input_file = easygui.fileopenbox(f'Виберіть файл {file_name}')
    print(f'Вибран файл {input_file}')
    return input_file
