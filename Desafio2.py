import os


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def get_degrees(notes):
    degree = {
        'dó': 'I',
        'ré': 'II',
        'mi': 'III',
        'fá': 'IV',
        'sol': 'V',
        'lá': 'VI',
        'si': 'VII',
        # abaixo notas musicais sem acentuação
        'do': 'I',
        're': 'II',
        'fa': 'IV',
        'la': 'VI',
    }
    return [degree.get(note.lower(), 'nota não encontrada') for note in notes]


clear_console()
aux = '1'
while aux == '1' or aux == 'sim':
    clear_console()

    print('Conversor de notas musicais;\n')
    notes = []
    a = 1
    for i in range(10):
        print(f"Por favor, informe a {a}ª nota musical: ")
        value = input()
        notes.append(value)
        a += 1

    print('\nOs valores da notas musicais informadas são respectivamente: \n',
          get_degrees(notes))
    aux = input(
        '\nDeseja fazer uma nova conversão?\n1-  sim\n2-  nao\n Escolha uma das opções acima:  ')
