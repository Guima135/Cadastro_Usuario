from datetime import datetime
data_cadastro = datetime.now()


def mostrar_opcoes():
    return print('Escolha uma das seguintes opções do sistema:\n'
                 '(1) adicionar usuário, '
                 '(2) remover usuário, '
                 '(3) alterar apelido, '
                 '(4) visualizar lista de usuários, '
                 '(5) sair')


def opcao():
    while True:
        try:
            return int(input('\nOpção: '))
        except ValueError:
            print("\nPor favor, digite um número inteiro, dente 1 a 5.")


def inserir_apelido():
    global apelido
    apelido = input('Insira apelido: ')
    try:
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if f'Código: {apelido}' in linha:
                    print("Usuário já existe no arquivo.\n")
                    return
    except FileNotFoundError:
        with open('usuarios.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('Lista de usuários: ')


def inserir_nome():
    global nome_completo
    while True:
        nome = input('Insira primeiro nome: ')
        sobrenome = input('Insira um sobrenome: ')
        if nome.isalpha() and sobrenome.isalpha():
            nome_completo = nome.capitalize() + ' ' + sobrenome.capitalize()
            print('Nome inserido: ', nome_completo)
            break
        else:
            print('Insira o formato correto!\n')


def inserir_idade():
    global idade
    while True:
        try:
            idade = int(input('Insira idade: '))
            if idade >= 18:
                break
            else:
                print('A idade deve ser maior do que 18 anos!\n')
        except ValueError:
            print('A idade deve ser um número inteiro!\n')


def inserir_genero():
    global genero
    print('Escolha um gênero: '
          '(1) Masculino, '
          '(2) Feminino, '
          '(3) Não Binário, '
          '(4) Outro\n')

    while True:
        escolher = int(input('Opção: '))
        if escolher == 1:
            genero = 'Masculino'
            break

        elif escolher == 2:
            genero = 'Feminino'
            break
        elif escolher == 3:
            genero = 'Não Binário'
            break
        elif escolher == 4:
            genero = input('Insira seu gênero: ')
            break
        else:
            print('Opção inválida!\n')

    print('Gênero inserido:', genero.capitalize(), '\n')


def cadastrar_usuario(usuarios):
    global nome_completo

    inserir_apelido()
    inserir_nome()
    inserir_idade()
    inserir_genero()

    data = data_cadastro.strftime("%Y-%m-%d")
    usuarios[apelido] = {'nome': nome_completo, 'idade': idade, 'gênero': genero, 'data_cadastro': data}

    with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f' Código: {apelido}| '
                      f'Nome: {nome_completo}| '
                      f'Idade: {idade}| '
                      f'Gênero: {genero}| '
                      f'Data de cadastro: {data}\n')
        print('Usuário cadastrado.\n')


def alterar_apelido(usuarios):
    apelido_buscado = input('Insira apelido para busca: ')

    for apelido in usuarios:
        while True:
            if apelido == apelido_buscado:
                novo_apelido = input('Insira novo apelido: ')
                if novo_apelido not in usuarios:
                    usuarios[apelido] = novo_apelido
                    break
            else:
                print('Usuário não encontrado!')


def remover_usuario():
    usuario_para_excluir = input('Digite o apelido do usuário a ser excluído: ')

    with open('usuarios.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    for linha in linhas:
        if usuario_para_excluir in linha:
            with open('usuarios.txt', 'w', encoding='utf-8') as f:
                for trecho in linhas:
                    if usuario_para_excluir not in trecho:
                        f.write(trecho)

        else:
            print("Linha não encontrada nesta linha")


def exibir_lista_usuarios():
    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()

    alunos_totais = []
    for linha in conteudo:
        alunos_totais.append(linha)

    for i, linha in enumerate(alunos_totais, 1):
        print(f'{i}.{linha}')
