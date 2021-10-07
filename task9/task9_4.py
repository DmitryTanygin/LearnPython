ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """

    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status


def convert_config_to_dict(config_filename):
    result = {}
    with open(config_filename) as f:
        for line in f:
            if line == '\n':
                continue
            if not line.startswith('!') and not ignore_command(line, ignore):
                if not line.startswith(' '):
                    key = line.rstrip()
                    result[key] = []
                else:
                    result[key].append(line)
        print(result)


convert_config_to_dict('config_sw1.txt')

