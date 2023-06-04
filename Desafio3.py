import os
import re

from datetime import datetime

aux = ''


def clear_console():  # Função feita exclusivamente para limpar a tela do console
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


clear_console()


def lower_value(value):  # Faz a separação da notas de baixo valor, de 20 a 2
    bills = []
    bill_2 = 0

    bill_20 = int(value // 20)
    value %= 20
    bill_10 = int(value // 10)
    value %= 10

    # verifica se o value é igual a 2 ou 8 para que no final não sobre 1 real
    if value == 6 or value == 8:
        bill_2 = int(value // 2)
        value %= 2

    bill_5 = int(value // 5)
    value %= 5

    if value != 0:
        bill_2 = int(value // 2)

    # Associa ao array bills a quantidade de notas
    if bill_20 > 0:
        bills.append(f"{bill_20} x 20 reais")
    if bill_10 > 0:
        bills.append(f"{bill_10} x 10 reais")
    if bill_5 > 0:
        bills.append(f"{bill_5} x 5 reais")
    if bill_2 > 0:
        bills.append(f"{bill_2} x 2 reais")

    # Impressão da divisão
    print("\n-- Distribuição de notas de menor valor:")
    for bill in bills:
        print(f"-   {bill}")
    return


# Faz a separação da notas de alto valor, de 100 a 50, com as sobras em notas menores
def highest_value(value):
    bill = []
    bill_2 = 0

    bill_100 = int(value // 100)
    value %= 100
    bill_50 = int(value // 50)
    value %= 50
    bill_20 = int(value // 20)
    value %= 20
    bill_10 = int(value // 10)
    value %= 10

    # verifica se o value é igual a 2 ou 8 para que no final não sobre 1 real
    if value == 6 or value == 8:
        bill_2 = int(value // 2)
        value %= 2

    bill_5 = int(value // 5)
    value %= 5

    if value != 0:
        bill_2 = int(value // 2)

    # Associa ao array bills a quantidade de notas
    if bill_100 > 0:
        bill.append(f"{bill_100} x 100 reais")
    if bill_50 > 0:
        bill.append(f"{bill_50} x 50 reais")
    if bill_20 > 0:
        bill.append(f"{bill_20} x 20 reais")
    if bill_10 > 0:
        bill.append(f"{bill_10} x 10 reais")
    if bill_5 > 0:
        bill.append(f"{bill_5} x 5 reais")
    if bill_2 > 0:
        bill.append(f"{bill_2} x 2 reais")

    # Impressão da divisão
    print("\n-- Distribuição de notas de maior valor:")
    for bill in bill:
        print(f"-   {bill}")
    return


def half_helper(value, aux):  # Faz a separação da notas meio a meio
    bills = []
    bill_2 = 0
    bill_5 = 0
    bill_10 = 0
    bill_20 = 0
    bill_50 = 0
    bill_100 = 0

    # Faz a verificação se é a primeira chamada da função, onde é necessario separar por notas de maiores valores
    if aux == 0:
        bill_100 = int(value // 100)
        value %= 100

        if value == 53:
            bill_20 = 2
            bill_5 = 1
            bill_2 = 4
            value = 0

        if value == 51:
            bill_20 = 2
            bill_5 = 1
            bill_2 = 3
            value = 0

        bill_50 = int(value // 50)
        value %= 50

        if bill_100 > 0:
            bills.append(f"{bill_100} x 100 reais")
        if bill_50 > 0:
            bills.append(f"{bill_50} x 50 reais")

    # Caso seja a segunda chamada, assim a var aux tendo valor 1, o código executa a separação apenas de notas de menores valores
    # Os ifs abaixo verificam se o value é um valor específico, para que não haja sobra no final
    if value == 43:
        bill_20 = 1
        bill_10 = 1
        bill_5 = 5
        bill_2 = 4
        value = 0

    if value == 41:
        bill_20 = 1
        bill_10 = 1
        bill_5 = 5
        bill_2 = 3
        value = 0

    if value == 23:
        bill_10 = 1
        bill_5 = 1
        bill_2 = 4
        value = 0

    if value == 21:
        bill_10 = 1
        bill_5 = 1
        bill_2 = 3
        value = 0
    # valores inferiores a 20 acabam aqui

    if value > 0:
        bill_20 = int(value // 20)
        value %= 20

    # Os ifs abaixo verificam se o value é um valor específico, para que não haja sobra no final
    if value == 13:
        bill_5 = 1
        bill_2 = 4
        value = 0

    if value == 11:
        bill_5 = 1
        bill_2 = 3
        value = 0
    # valores inferiores a 10 acabam aqui

    if value > 0:
        bill_10 = int(value // 10)
        value %= 10
    # Verifica se o value é igual a 6 ou a 8 para que a divisão seja feita apenas em nota de 2 reais
    if value == 6 or value == 8:
        bill_2 = int(value // 2)
        value %= 2

    if value > 0:
        bill_5 = int(value // 5)
        value %= 5

    if value > 0:
        bill_2 = int(value // 2)

    # Associa ao array bills a quantidade de notas
    if bill_20 > 0:
        bills.append(f"{bill_20} x 20 reais")
    if bill_10 > 0:
        bills.append(f"{bill_10} x 10 reais")
    if bill_5 > 0:
        bills.append(f"{bill_5} x 5 reais")
    if bill_2 > 0:
        bills.append(f"{bill_2} x 2 reais")
    return bills


def half_value(value):  # Essa função auxilia a chamada da função half_helper
    value = int(value / 2)
    half = value

    # Primeira chamada com divisão por notas maiores
    bills_1 = half_helper(value, 0)
    # Segunda chamada com divisão por notas menores
    bills_2 = half_helper(value, 1)

    # Impressão das divisões
    print("\n-- Distribuição de notas meio a meio:")
    print(f"\n-   {half} reais em notas de maior valor:")
    for nota in bills_1:
        print(f"-    {nota}")

    print(f"\n-   {half} reais em notas de menor valor:")
    for bill in bills_2:
        print(f"-    {bill}")
    return


# Possui a funcionalidade de redirecionar a execução para o tipo de divisão escolhida
def redirector(loan_amount, aux):

    # Notas de maior valor
    if aux == 1:
        print(f"\n-   Valor de empréstimo: {loan_amount}")
        highest_value(loan_amount)

    # Notas de menor valor
    elif aux == 2:
        print(f"\n-   Valor de empréstimo: {loan_amount}")
        lower_value(loan_amount)

    # Notas meio a meio
    elif aux == 3:
        print(f"\n-   Valor de empréstimo: {loan_amount}")
        half_value(loan_amount)

    # Caso a opção digitada não exista
    else:
        print('\n-- Opção não encontrada, por favor tente novamente;')


# Possui a funcionalidade de mostrar ao contribuinte a opções de divisão de notas e permitir que ele escolha e troque de escolha
def choose_bill(loan_amount):
    global aux
    aux = ''
    clear_console()

    # Impressão das opções
    print(f"\nO sistema disponibiliza apenas a retirada em dinheiro, por favor, selecione uma das seguintes opções:\n")
    print(f" 1- nota de maior valor: considerando primeiramente as nota de 100 e 50 reais, e em seguida, as inferiores.")
    print(f" 2- nota de menor valor: considerando as nota de 20, 10, 5 e 2 reais.")
    print(f" 3- nota meio a meio: metade do valor em notas maiores e a outra metade em notas menores.")

    # Loop de verificação
    while isinstance(aux, str):
        try:
            aux = int(
                input(" -    Digite o número da opção desejada: "))

            # Caso não haja nenhum erro, chama a função de redirecionamento
            redirector(loan_amount, aux)
        except ValueError:
            # Caso de erro, o sistema verifica se o contribuinte digitou um valor string invés de int
            if isinstance(aux, str):
                print(
                    '\nValor inválido. Por favor, insira o número de uma das opções listadas.')
                continue

            # Verifica se o valor foi float invés de int
            if isinstance(aux, float):
                print(
                    '\nValor inválido. Por favor, insira o número de uma das opções listadas.')
                continue

    # Parte que permite o contribuinte trocar de opção
    choose = ''

    # Loop de verificação
    while choose != 'nao':
        print(
            '\nDeseja alterar a forma de distribuição de notas? (Responda com sim ou nao) ')
        choose = input()

        if choose == 'sim':
            # Chama denovo a função de escolha
            choose_bill(loan_amount)
        elif choose == 'nao':
            # Sai da parte de escolha
            continue

        # Mostra mensagem de erro
        else:
            print('Opção inválida;')


# Possui a funcionalidade de receber a data de admissão e verificar se a data inserida não possui um valor futuro
def get_date():

    # Loop de verificação
    while True:
        date_str = input("- Digite a data de admissão (formato: dd/mm/aaaa): ")

        try:
            date = datetime.strptime(date_str, "%d/%m/%Y")

            # Verifica se a data atual é inferior a data inserida
            if date > datetime.now():
                print("\nData futura inserida. Por favor, insira uma data válida.")

            # Se for válida retorna a data
            else:
                return date
        # E caso a data seja inválida, mostra a seguinte mensagem
        except ValueError:
            print("\nData inválida. Por favor, insira uma data no formato correto.")


# Possui a funcionalidade de verificar se o nome inserido pelo contribuinte possui apenas letras e espaços
def check_string(string):
    standard = r'^[a-zA-ZÀ-ÿ\s]+$'
    return re.match(standard, string) is not None


# Possui a funcionalidade de pegar os dados númericos do contribuinte, salário e valor do empréstimo
def get_value(type):
    current = ''

    # Verificação para mudar o texto que é impresso
    if type == 0:
        text_aux = ['- Digite o salário atual do colaborador:',
                    'Seu salário não pode ser negativo, por favor tente novamente;']
    else:
        text_aux = ['- Digite o valor do empréstimo desejado: ',
                    'O empréstimo não pode ter uma valor negativo, por favor tente novamente;']

    # Loop de verificação
    while isinstance(current, str):
        try:
            current = int(input(text_aux[0]))
            if current > 0:
                return current

        # Caso o valor da variável current não seja int
        except:

            # Verificação se é do tipo string
            if isinstance(current, str):
                print('\nValor inválido. Por favor, insira um número inteiro.')
                value = input(text_aux[0])

                try:
                    # Transforma em int se o valor for numérico
                    value = int(value)
                    if value > 0:
                        return value

                # Verifica se o valor é do tipo string
                except:
                    if isinstance(value, str):
                        print(
                            '\nValor inválido. Por favor, insira um número inteiro.')
                        continue

            # Verifica se o valor é do tipo float
            if isinstance(current, float):
                print('Valor inválido. Por favor, insira um número inteiro.')
                continue
        current = -1
        # Loop que verifica se a var current é positiva
        while current < 0:
            print(f'\nValor inválido. Por favor, insira um número inteiro.')

            try:
                current = int(input(text_aux[0]))
            except:
                print('\nValor inválido. Por favor, insira um número inteiro.')
                value = input(text_aux[0])
                try:
                    # Transforma em int se o valor for numérico
                    value = int(value)
                    current = value

                except:
                    # Verifica se o valor é do tipo string
                    if isinstance(value, str):
                        continue

    return current


def aux_fun(contributor_name, home_time, current_wage):
    # Caso o tempo de casa seja superior a 5 anos
    if home_time > 5:

        # Chama a função get_value para pegar o valor do empréstimo
        loan_amount = get_value(1)

        # Verifica se o valor do empréstimo é até 2 vezes o salári atual do contribuinte e se é um valor par
        if current_wage * 2 < loan_amount or loan_amount % 2 != 0:
            print(
                "- Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
            return
        # Chama a função de escolha de distribuição
        choose_bill(loan_amount)
        clear_console()

        # Imprime os dados do contrinuinte
        print('- Dados do Contribuinte: ')
        print(f'-   Nome do contribuinte: {contributor_name}')
        print(f'-   Tempo de casa: {home_time}')
        print(f'-   Salário atual: {current_wage}')

        print('\n- Dados do Empréstimo:')

        # Chama o redirecionador denovo para que seja reimpressa a distribuiço de notas escolhida
        redirector(loan_amount, aux)

        print('\nDeseja refazer a simulação? (responda com sim ou nao)')
        if input() == 'sim':
            make_loan()
        else:
            print(
                "\nPor favor, vá a uma de nossas agências parceiras para poder retirar o dinheiro.")
    else:
        print("\n- Não é possível realizar o empréstimo. Tempo de casa insuficiente.")


# Função principal do sistema, é a primeira função a ser chamada e é nela que estão as primeria inserções
def make_loan():
    # Limpa a tela do console
    clear_console()

    contributor_name = input("- Digite o nome do colaborador: ")

    # Loop que verifica se o nome do contribuinte é válido
    while check_string(contributor_name) == False:
        print("\nSeu nome deve conter apenas letra, com ou sem acentos, e espaços, por favor tente novamente;")
        contributor_name = input("- Digite o nome do colaborador: ")

    # Chama a função de obter data de admissão
    admission_date = get_date()

    # Chama a função get_value para pegar o valor do sálario atual
    current_wage = get_value(0)

    current_date = datetime.now().date()
    home_time = current_date.year - admission_date.year

    # Verifica se a data atual é anterior à data de admissão com base no mês e dia
    if current_date.month < admission_date.month or (current_date.month == admission_date.month and current_date.day < admission_date.day):
        home_time -= 1
        aux_fun(contributor_name, home_time, current_wage)
    else:
        aux_fun(contributor_name, home_time, current_wage)


make_loan()
