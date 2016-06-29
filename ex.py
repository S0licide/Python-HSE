import re


def op(path):
    file = open(path, 'r', encoding='utf-8')
    string = file.read()
    file.close()
    return string


def srch_names(string):
    res = re.findall('[А-Я]\.+\s+[А-Я][а-я]+', string)
    print(res)


def main():
    path = input('Введите путь к файлу: ')
    srch_names(op(path))

main()