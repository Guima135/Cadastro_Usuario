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


def exibir_usuario_adicionado(alunos):
    print('Alunos adicionados:')
    for usuario, valores in alunos.items():
        print(f' Código: {usuario}| Nome: {valores['nome']}| Idade: {valores['idade']}| Gênero: {valores['gênero']}\n')


def adicionar_usuario(usuarios):

    apelido = input('Insira apelido: ')
    nome = input('Insira nome: ')
    idade = int(input('Insira idade: '))
    genero = input('Insira genero: ')

    usuarios[apelido] = {'nome': nome, 'idade': idade, 'gênero': genero}
    try:
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if f'Código: {apelido}' in linha:
                    print("Usuário já existe no arquivo.")
                    return

    except FileNotFoundError:
        with open('usuarios.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('Lista de usuários: ')

    with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f' Código: {apelido}| Nome: {nome}| Idade: {idade}| Gênero: {genero}\n')
        print('Usuário cadastrado')


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
