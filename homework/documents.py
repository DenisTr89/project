def return_help():
    return print("Список доступных команд:\n\
    Пользователь по команде 'p' может узнать владельца документа по его номеру\n\
    Пользователь по команде 's' может по номеру документа узнать на какой полке он хранится\n\
    Пользователь по команде 'l' может увидеть полную информацию по всем документам\n\
    Пользователь по команде 'ads' может добавить новую полку\n\
    Пользователь по команде 'ds' может удалить существующую полку из данных (только если она пустая)\n\
    Пользователь по команде 'help' может узнать список всех команд\n\
    Выход из программы 'q'")

return_help()

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def return_by_number():
    """Пользователь по команде "p" может узнать владельца документа по его номеру"""
    for i in documents:
        if i['number'] == command:
            return print(f"Владелец документа: {i['name']}")
    print("Документ не найден в базе")

def return_number_on_shelf():
    """Пользователь по команде "s" может по номеру документа узнать на какой полке он хранится"""
    
    for i in range(1, len(directories)):
        if command in directories[f"{i}"]:
            return print(f"Документ хранится на полке: {i}")
    print("Документ не найден в базе")

def return_all_information():
    """Пользователь по команде "l" может увидеть полную информацию по всем документам"""

    for i in range(0, len(documents)):
        print(f"№: {documents[i]['number']}, тип: {documents[i]['type']}, владелец: {documents[i]['name']}, \
полка хранения: {''.join([key for key, values in directories.items() if documents[i]['number'] in values])}")

def return_add_shelf():
    """Пользователь по команде "ads" может добавить новую полку"""

    if command in directories.keys():
        return print(f"Такая полка уже существует. Текущий перечень полок: {' '.join(list(directories.keys()))}.")
    else:
        if command.count(" ") == 0:
            directories[command] = []
            return print(f"Полка добавлена. Текущий перечень полок: {' '.join(list(directories.keys()))}")
        else:
            return print("Полка вводится без пробела")

def return_del_shelf():
    """Пользователь по команде "ds" может удалить
    существующую полку из данных (только если она пустая)
    """

    for key, value in directories.items():
        if key == command and value == []:
            directories.pop(key)
            print(f"Полка удалена. Текущий перечень полок: {' '.join(list(directories.keys()))}")
            return directories
        elif key == command and value != []:
            print(f"На полке есть документы, удалите их перед удалением полки.Текущий перечень полок: {' '.join(list(directories.keys()))}.")
            return directories
    print(f"Такой полки не существует. Текущий перечень полок: {' '.join(list(directories.keys()))}")


command = input("Введите команду: ")
while command != "q":
    if command == "p":
        command = input("Введите номер документа: ")
        return_by_number()
    elif command == "s":
        command = input("Введите номер документа: ")
        return_number_on_shelf()
    elif command == "l":
        return_all_information()
    elif command == "ads":
        command = input("Введите номер полки: ")
        return_add_shelf()
    elif command == "ds":
        command = input("Введите номер полки: ")
        return_del_shelf()
    elif command == "help":
        return_help()
    command = input("Введите команду: ")
    
