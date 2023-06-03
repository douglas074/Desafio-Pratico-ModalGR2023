import os


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


clear_console()
print('\nVerificador de repetições;\n')

print("Informe os valores do primeiro array: ")
# Entrada dos valores do segundo array
a = 1
first_array = []
for i in range(5):
    value = ''
    while isinstance(value, str):
        try:
            value = int(input('Informe o ' + str(a) + 'º valor: '))
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro.')
            value = input('Informe o ' + str(a) + 'º valor: ')
            try:
                value = int(value)
            except:
                if isinstance(value, str):
                    print('Valor inválido. Por favor, insira um número inteiro.')
                    continue
        first_array.append(value)
    a += 1


# Entrada dos valores do segundo array
second_array = []
a = 1
print("\nInforme os valores do segundo array: ")
for i in range(5):
    value = ''
    while isinstance(value, str):
        try:
            value = int(input('Informe o ' + str(a) + 'º valor: '))
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro.')
            value = input('Informe o ' + str(a) + 'º valor: ')
            try:
                value = int(value)
            except:
                if isinstance(value, str):
                    print('Valor inválido. Por favor, insira um número inteiro.')
                    continue
        second_array.append(value)
    a += 1


def find_repeats(first_array, second_array):
    repetitions = []
    for num in first_array:
        if num in second_array and num not in repetitions:
            repetitions.append(num)
    return repetitions


print("Os valores repetidos em ambos os array são: ",
      find_repeats(first_array, second_array))
