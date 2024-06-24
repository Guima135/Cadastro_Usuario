import re
import json
from datetime import datetime, date
data_cadastro = datetime.now()
users = {}

age = None
nickname = None
name = None
genero = None
email = None
endereco = None


def show_options():
    return print('Choose one of the following options:\n'
                 '(1) Create User, '
                 '(2) Remove User, '
                 '(3) Alter Information, '
                 '(4) Visualize Registered Users, '
                 '(5) Exit')


def option():
    while True:
        try:
            return int(input('\nOption: '))
        except ValueError:
            print("\nYou must insert an integer between 1 and 5")


def inserir_apelido():
    global nickname
    nickname = input('Insert nickname: ')
    try:
        with open("dados.json", "r", encoding='utf-8') as file:
            json_data = json.load(file)
            if nickname in json_data:
                print("Nickname already in use.\n")
                return False
        return True
    except FileNotFoundError:
        return True


def inserir_nome():
    global name
    while True:
        first_name = input('Insira primeiro nome: ')
        sobrenome = input('Insira um sobrenome: ')
        if first_name.isalpha() and sobrenome.isalpha():
            name = first_name.capitalize() + ' ' + sobrenome.capitalize()
            print('Nome inserido: ', name)
            break
        else:
            print('Insira o formato correto!\n')


def inserir_data_nascimento():
    global age

    while True:
        try:
            nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
            nascimento_date = datetime.strptime(nascimento, "%d/%m/%Y").date()
        except ValueError:
            print('Formato incorreto')
            continue

        hoje = date.today()
        age = hoje.year - nascimento_date.year
        if hoje.month < nascimento_date.month or \
                (hoje.month == nascimento_date.month and hoje.day < nascimento_date.day):
            age -= 1
        if age >= 18:
            break
        else:
            print('Você não deve ter menos de 18 anos!')


def inserir_genero():
    global genero
    print('Choose a gender: '
          '(1) Male, '
          '(2) Female, '
          '(3) Non-binary, '
          '(4) Other\n')

    while True:
        choose = int(input('Option: '))
        if choose == 1:
            genero = 'Male'
            break
        elif choose == 2:
            genero = 'Female'
            break
        elif choose == 3:
            genero = 'Non-binary'
            break
        elif choose == 4:
            genero = input('Insira seu gênero: ')
            break
        else:
            print('Opção inválida!\n')

    print('Gênero inserido:', genero.capitalize(), '\n')


def inserir_email():
    global email
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input("Por favor, insira seu e-mail: ")
        if re.match(padrao_email, email):
            print("E-mail válido.")
            break
        else:
            print("Formato de e-mail inválido. Tente novamente.")


def inserir_endereco():
    global endereco

    logradouro = input('Logradouro: ')
    while True:
        numero = input('Número: ')
        if numero.isdigit():
            break
        else:
            print('Valor incorreto.\n')

    cidade = input('Cidade: ')
    estado = input('Estado: ')
    while True:
        cep = input('CEP: ')
        if len(cep) == 8 and cep.isdigit():
            break
        else:
            print('O CEP deve possuir 8 dígitos numéricos.\n')

    endereco = f"{logradouro}, {numero} - {cidade}/{estado} - {cep}"


def cadastrar_usuario():
    global users
    global data_cadastro

    if not inserir_apelido():
        return

    inserir_nome()
    inserir_data_nascimento()
    inserir_genero()
    inserir_email()
    inserir_endereco()

    data_cadastro = datetime.now()
    data = data_cadastro.strftime("%Y-%m-%d")

    try:
        with open("dados.json", "r", encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    users[nickname] = {
        'name': name,
        'age': age,
        'gender': genero,
        'email': email,
        'data_cadastro': data,
        'endereco': endereco,
    }

    with open("dados.json", "w", encoding='utf-8') as file:
        json.dump(users, file, indent=4)
        print('Usuário cadastrado.\n')


def alterar_dados():
    with open("dados.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)
        try:
            usuario_buscado = input('Selecione um usuário: ')
            resultado_busca = json_data[usuario_buscado]
        except KeyError:
            print('Usuário não encontrado')
        else:
            print(resultado_busca)
            print('\nEscolha um dado para ser alterado:\n'
                  'Nome (1),'
                  'E-mail (2),'
                  'Endereço (3),'
                  'Sair (4) ')

            escolher = int(input('\nOpção: '))
            if escolher == 1:
                inserir_nome()
                json_data[usuario_buscado]['name'] = name
            if escolher == 2:
                inserir_email()
                json_data[usuario_buscado]['email'] = email
            if escolher == 3:
                inserir_endereco()
                json_data[usuario_buscado]['endereco'] = endereco
            if escolher == 4:
                show_options()

            with open('dados.json', 'w', encoding='utf-8') as file:
                json.dump(json_data, file, indent=4)


def remover_usuario():
    with open("dados.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)
        try:
            usuario_buscado = input('Selecione um usuário: ')
            resultado_busca = json_data[usuario_buscado]
        except KeyError:
            print('Usuário não encontrado')
        else:
            print(resultado_busca)
            del json_data[usuario_buscado]
            with open("dados.json", "w", encoding='utf-8') as file:
                json.dump(json_data, file, indent=4)
            print('Usuário removido')


def exibir_lista_usuarios():
    with open("dados.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)
    print(json.dumps(json_data, indent=4))


if __name__ == "__main__":
    cadastrar_usuario()
