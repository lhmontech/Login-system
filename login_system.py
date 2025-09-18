usuarios = {'Admin':'123456'}
bloqueados = set()

while True:
    print('\nBem vindo ao sistema de login lhmontech!\n 1- Entrar\n 2- Sair')
    opcao = int(input('\nDigite o que gostaria de fazer:'))
    match opcao:
        case 1:
            while True:
                usuario = input('Digite o seu nome de usuário:')
                if usuario in bloqueados:
                    print('Usuário bloqueado!')
                elif usuario in usuarios:
                    for i in range(1,4):
                        senha = input('\nDigite sua senha:')
                        if senha == usuarios[usuario]:
                            print(f'\nBem vindo, {usuario}!')
                            while True:
                                opcao = int(input('\nSelecione uma opção:\n'
                                                  ' 1- Usuários cadastrados\n 2- Cadastrar novo usuário\n 3- Remover usuário\n 4- Sair '))
                                match opcao:
                                    case 1:
                                        print('lista de usuários cadastrados:')
                                        print(f'- {usuarios[usuario]}')
                                    case 2:
                                        print('Área de cadastro.')
                                        usuario = input('Digite o nome do usuario: ')
                                        usuarios[usuario] = input('Digite a senha: ')
                                    case 3:
                                        print('Remover de usuário')
                                    case 4:
                                        break
                                    case _:
                                        print('Selecione uma opção válida!')
                            break
                        else:
                            print('Senha incorreta!')
                    print('\nTentativas esgotadas!')
                    bloqueados.add(usuario)
                    break
                else:
                    print('Usuário incorreto!\n')
        case 2:
            break
        case _:
            print('Erro! Opção inválida!')

print('Fim do programa!')

