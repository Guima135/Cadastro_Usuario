from cadastro_de_usuario_funcoes import *

print('Account Creation System:\n')
chosen_option = 0

while chosen_option != 5:
    show_options()
    chosen_option = option()

    if chosen_option == 1:
        cadastrar_usuario()

    elif chosen_option == 2:
        remover_usuario()

    elif chosen_option == 3:
        alterar_dados()

    elif chosen_option == 4:
        pass

    elif chosen_option == 5:
        print('Sistema encerrado')

    else:
        print('\nOpção inválida! Escolha um dos cinco números!\n')
