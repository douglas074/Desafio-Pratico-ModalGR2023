import os
from datetime import datetime

aux = 0


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


clear_console()


def calculate_grades(value, aux):
    value = int(value)
    if aux == 1:
        bill = []
        bill_2 = 0
        # Cálculo das valor de maior valor
        # Notas de R$100
        bill_100 = int(value // 100)
        value %= 100

        # Notas de R$50
        bill_50 = int(value // 50)
        value %= 50

        # Notas de R$20
        bill_20 = int(value // 20)
        value %= 20

        # Notas de R$10
        bill_10 = int(value // 10)
        value %= 10

        if value == 6 or value == 8:
            bill_2 = int(value // 2)
            value %= 2
        # Notas de R$5
        bill_5 = int(value // 5)
        value %= 5

        # Notas de R$2
        if value != 0:
            bill_2 = int(value // 2)

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

        print("\n-- Distribuição de notas de maior valor:")
        for nota in bill:
            print(f"-   {nota}")
        return

    if aux == 2:
        bills = []
        bill_2 = 0
        # Cálculo das notas de menor valor

        # Notas de R$20
        bill_20 = int(value // 20)
        value %= 20

        # Notas de R$10
        bill_10 = int(value // 10)
        value %= 10

        if value == 6 or value == 8:
            bill_2 = int(value // 2)
            value %= 2
        # Notas de R$5
        bill_5 = int(value // 5)
        value %= 5

        # Notas de R$2
        if value != 0:
            bill_2 = int(value // 2)

        if bill_20 > 0:
            bills.append(f"{bill_20} x 20 reais")
        if bill_10 > 0:
            bills.append(f"{bill_10} x 10 reais")
        if bill_5 > 0:
            bills.append(f"{bill_5} x 5 reais")
        if bill_2 > 0:
            bills.append(f"{bill_2} x 2 reais")

        print("\n-- Distribuição de notas de menor valor:")
        for nota in bills:
            print(f"-   {nota}")
        return

    if aux == 3:
        value = int(value / 2)
        half = value
        bills_1 = []
        bills_2 = []
        bill_2 = 0
        bill_5 = 0
        bill_10 = 0
        bill_20 = 0

        # Cálculo das notas de maior valor
        # Notas de R$100
        bill_100 = int(value // 100)
        value %= 100

        # Notas de R$50
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

        # Notas de R$20
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

        # Notas de R$10
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

        if value > 0:
            bill_20 = int(value // 20)
            value %= 20

        if value == 13:
            bill_5 = 1
            bill_2 = 4
            value = 0

        if value == 11:
            bill_5 = 1
            bill_2 = 3
            value = 0

        if value > 0:
            bill_10 = int(value // 10)
            value %= 10

        if value == 6 or value == 8:
            bill_2 = int(value // 2)
            value %= 2
        # Notas de R$5
        if value > 0:
            bill_5 = int(value // 5)
            value %= 5

        # Notas de R$2
        if value > 0:
            bill_2 = int(value // 2)

        if bill_100 > 0:
            bills_1.append(f"{bill_100} x 100 reais")
        if bill_50 > 0:
            bills_1.append(f"{bill_50} x 50 reais")
        if bill_20 > 0:
            bills_1.append(f"{bill_20} x 20 reais")
        if bill_10 > 0:
            bills_1.append(f"{bill_10} x 10 reais")
        if bill_5 > 0:
            bills_1.append(f"{bill_5} x 5 reais")
        if bill_2 > 0:
            bills_1.append(f"{bill_2} x 2 reais")

        value = half
        # Cálculo das notas de menor valor
        # Notas de R$20
        bill_20 = int(value // 20)
        value %= 20

        # Notas de R$10
        bill_10 = int(value // 10)
        value %= 10
        # valor ser menor 53 terminar em 1 ou 3
        if value == 6 or value == 8:
            bill_2 = int(value // 2)
            value %= 2
        # Notas de R$5
        bill_5 = int(value // 5)
        value %= 5

        # Notas de R$2
        if value != 0:
            bill_2 = int(value // 2)

        if bill_20 > 0:
            bills_2.append(f"{bill_20} x 20 reais")
        if bill_10 > 0:
            bills_2.append(f"{bill_10} x 10 reais")
        if bill_5 > 0:
            bills_2.append(f"{bill_5} x 5 reais")
        if bill_2 > 0:
            bills_2.append(f"{bill_2} x 2 reais")

        print("\n-- Distribuição de notas meio a meio:")
        print(f"\n-   {half} reais em notas de maior valor:")
        for nota in bills_1:
            print(f"-    {nota}")

        print(f"\n-   {half} reais em notas de menor valor:")
        for nota in bills_2:
            print(f"-    {nota}")
        return


def choose_bill(loan_amount):
    global aux
    clear_console()
    print(f"\nO sistema disponibiliza apenas a retirada em dinheiro, por favor, selecione uma das seguintes opções:\n")
    print(f" 1- nota de maior valor: considerando primeiramente as nota de 100 e 50 reais, e em seguida, as inferiores.")
    print(f" 2- nota de menor valor: considerando as nota de 20, 10, 5 e 2 reais.")
    print(f" 3- nota meio a meio: metade do valor em notas maiores e a outra metade em notas menores.")
    aux = 0
    while aux != 1 and aux != 2 and aux != 3:
        aux = int(input(" -    Digite o número da opção desejada: "))
        if aux == 1 or aux == 2:
            print(f"\n-- Valor do empréstimo: {loan_amount} reais")
            calculate_grades(loan_amount, aux)
            choose = ''
            while choose != 'sim' and choose != 'nao':
                print(
                    '\nDeseja alterar a forma de distribuição de notas? (Responda com sim ou nao) ')
                choose = input()

                if choose == 'sim':
                    choose_bill(loan_amount)
                elif choose == 'nao':
                    continue
                else:
                    print('Opção inválida;')

        elif aux == 3:
            print(f"\n-- Valor do empréstimo: {loan_amount} reais")

            calculate_grades(loan_amount, aux)
        else:
            print('\n-- Opção não encontrada, por favor tente novamente;')


def obter_data():
    while True:
        data_str = input("- Digite a data de admissão (formato: dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            if data > datetime.now():
                print("Data futura inserida. Por favor, insira uma data válida.")
            else:
                return data
        except ValueError:
            print("Data inválida. Por favor, insira uma data no formato correto.")


def realizar_emprestimo():
    clear_console()
    print('Simulador de emprestimos;\n')
    contributor_name = input("- Digite o nome do colaborador: ")
    admission_date = obter_data()
    current_wage = int(
        input("- Digite o salário atual do colaborador: "))
    while current_wage < 0:
        print('Seu salário não pode ser negativo, por favor tente novamente;')
        current_wage = float(
            input("- Digite o salário atual do colaborador: "))
    current_date = datetime.now().date()
    home_time = current_date.year - admission_date.year
    if current_date.month < admission_date.month or (current_date.month == admission_date.month and current_date.day < admission_date.day):
        home_time -= 1
        if home_time > 5:
            loan_amount = int(
                input("- Digite o valor de empréstimo desejado: "))
            while loan_amount < 0:
                print(
                    'O valor do empréstimo não pode ser negativo, por favor tente novamente;')
                loan_amount = float(
                    input("- Digite o salário atual do colaborador: "))
            if current_wage * 2 < loan_amount or loan_amount % 2 != 0:
                print(
                    "- Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
                return
            choose_bill(loan_amount)
            clear_console()
            print('- Dados do empreśtimo: \n')
            # posso fazer uma parte para mostrar os dados do emprestimo e se ele quer mudar a forma das bill ou algo assim
            print(f'-   Nome do contribuinte: {contributor_name}')
            print(f'-   Tempo de casa: {home_time}')
            print(f'-   Salário atual: {current_wage}')
            print(f'-   Valor de empréstimo: {loan_amount}')
            calculate_grades(loan_amount, aux)
            print('\nDeseja refazer a simulação? (responda com sim ou nao)\n')
            if input() == 'sim':
                realizar_emprestimo()
            else:
                print(
                    "\nPor favor, vá a uma de nossas agências parceiras para poder retirar o dinheiro.")
        else:
            print("\n- Não é possível realizar o empréstimo. Tempo de casa insuficiente.")


realizar_emprestimo()
