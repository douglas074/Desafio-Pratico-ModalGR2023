import os


def clear_console():  # Possui a funcionalidade de limpar a tela do console
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


# Possui a funcionalidade de relacionar a nota musical com o algarismo romano correspondente.
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

    # Retorna o valor romano correspondente, transforma letras maiúsculas em minúsculas para evitar erros de verificação.
    return [degree.get(note.lower(), 'nota não encontrada') for note in notes]


clear_console()  # Limpar console

aux = '1'

# Loop de verificação se a escolha de repetição é positivo
while aux == '1' or aux == 'sim' or aux == 's':
    clear_console()

    print('Conversor de notas musicais;\n')
    musical_notes = []
    notes = []
    a = 1

    # Loop para receber as notas musicais
    for i in range(10):
        print(f"Por favor, informe a {a}ª nota musical: ")
        value = input()
        musical_notes.append(value)
        notes.append(value)
        a += 1

    print('\nOs valores da notas musicais informadas são respectivamente: \n',
          musical_notes, '\n',
          get_degrees(notes))

    aux = input(
        '\nDeseja fazer uma nova conversão?\n  1-  sim\n  2-  nao\n  Escolha uma das opções acima:  ')

    # Loop de verificação caso a opção escolhida não exista
    while aux != 'sim' and aux != 'nao' and aux != 's' and aux != 'n' and aux != '1' and aux != '2':
        print('\nOpção não encontrada, por favor tente novamente')
        aux = input(
            'Deseja fazer uma nova conversão?\n  1-  sim\n  2-  nao\n  Escolha uma das opções acima:  ')
