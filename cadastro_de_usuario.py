from cadastro_de_usuario_funcoes import *

usuarios = {}

print('Sistema de cadastro de usuários:\n')
opcao_escolhida = 0

while opcao_escolhida != 5:
    mostrar_opcoes()
    opcao_escolhida = opcao()

    if opcao_escolhida == 1:
        adicionar_usuario(usuarios)

    elif opcao_escolhida == 2:
        remover_usuario()

    elif opcao_escolhida == 3:
        alterar_apelido(usuarios)

    elif opcao_escolhida == 4:
        exibir_lista_usuarios()

    elif opcao_escolhida == 5:
        print('Sistema encerrado')

    else:
        print('\nOpção inválida! Escolha um dos cinco números!\n')
