import os


def clear_console():  # Possui a funcionalidade de limpar a tela do console
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def get_values(type):  # Função que recebe os valores de ambos arrays
    array = []
    a = 1

    # Verificação que altera o texto que será exibido
    if type == 0:
        print("\nInforme os valores do primeiro array: ")
    else:
        print("\nInforme os valores do segundo array: ")

    # Loop de entrada de dados
    for i in range(5):
        value = ''

        # Loop que verifica se a var value é uma string, começa com valor string para poder entrar no loop
        while isinstance(value, str):
            try:
                value = int(input('-  Informe o ' + str(a) + 'º valor: '))

            # Caso o valor não seja int cai na exception abaixo
            except:
                print('Valor inválido. Por favor, insira um número inteiro.')
                value = input('-  Informe o ' + str(a) + 'º valor: ')

                # try except verifica se o valor pode ser convertido para int, caso contrário o valor é uma string
                try:
                    value = int(value)
                except:
                    if isinstance(value, str):
                        print('Valor inválido. Por favor, insira um número inteiro.')
                        continue

            array.append(value)
        a += 1

    return array


# Possui a funcionalidade de verifica se há reperições dentro de ambos os arrays
def find_repeats(first_array, second_array):

    repetitions = []
    for num in first_array:
        if num in second_array and num not in repetitions:
            repetitions.append(num)
    return repetitions


aux = 'sim'
# Loop de verificação se a escolha de repetição é positivo
while aux == '1' or aux == 'sim' or aux == 's':
    clear_console()
    print('Verificador de repetições;')

    # chaama a função get_values para receber os valores a serem comparados
    first_array = get_values(0)
    second_array = get_values(1)

    # Imprime as reperições que são encontradas na função find_repeats
    print("\nOs valores repetidos em ambos os array são: ",
          find_repeats(first_array, second_array))

    aux = input(
        '\nDeseja fazer uma nova comparação?\n  1-  sim\n  2-  nao\n\n- Escolha uma das opções acima:  ')

    # Loop de verificação caso a opção escolhida não exista
    while aux != 'sim' and aux != 'nao' and aux != 's' and aux != 'n' and aux != '1' and aux != '2':
        print('\nOpção não encontrada, por favor tente novamente')
        aux = input(
            'Deseja fazer uma nova comparação?\n  1-  sim\n  2-  nao\n  Escolha uma das opções acima:  ')
