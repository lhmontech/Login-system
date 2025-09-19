from colorama import init, Fore

init(autoreset=True)

usuarios = {'Admin':'123456','Lucas':'abcd','Pablo':'escobar'}
bloqueados = set()

while True:
    try:
        print('\nBem vindo ao sistema de login lhmontech!\n 1- Entrar\n 2- Cadastro\n 3- Sair')
        opcao = int(input('\nDigite o que gostaria de fazer:'))
        match opcao:
            case 1:
                while True:
                    for i in range(1,4):
                        usuario = input('\nDigite o seu nome de usuário:')
                        if usuario in bloqueados:
                            print(Fore.RED + '\nUsuário bloqueado!')
                        elif usuario in usuarios:
                            for i in range(1,4):
                                senha = input('\nDigite sua senha:')
                                if senha == usuarios[usuario]:
                                    print(f'\nBem vindo, {usuario}!')
                                    while True:
                                        opcao = int(input('\nSelecione uma opção:\n'
                                                          ' 1- Usuários cadastrados\n 2- Remover usuário\n 3- Usuários bloqueados\n'
                                                          ' 4- Desbloquear usuário\n 5- Sair '))
                                        match opcao:
                                            case 1:
                                                print('\nlista de usuários cadastrados:')
                                                print(*usuarios.keys(), sep='\n')
                                            case 2:
                                                usuario = input('\nDigite o nome de usuário que gostaria de remover:')
                                                del usuarios[usuario]
                                                print(Fore.BLUE + 'Usuário removido!')
                                            case 3:
                                                print('\nlista de usuários bloqueados:')
                                                print(*bloqueados, sep='\n')
                                            case 4:
                                                usuario = input('\nDigite o nome de usuário que gostaria de desbloquear:')
                                                bloqueados.remove(usuario)
                                                print(Fore.BLUE + 'Usuário desbloqueado!')
                                            case 5:
                                                break
                                            case _:
                                                print(Fore.RED + '\nSelecione uma opção válida!')
                                    break
                                else:
                                    print(Fore.RED + 'Senha incorreta!')
                            print(Fore.RED + '\nTentativas esgotadas!')
                            bloqueados.add(usuario)
                            break
                        else:
                            print(Fore.RED + 'Usuário incorreto!\n')
                    print(Fore.RED + '\nTentativas esgotadas!')
                    break
            case 2:
                print('Área de cadastro.')
                while True:
                    usuario = input('\nDigite o nome do usuario: ')
                    if usuario in usuarios:
                        print('\nNome de usuário já em uso!')
                    else:
                        usuarios[usuario] = input('Digite a senha: ')
                        print(Fore.BLUE + '\nCadastro realizado com sucesso!')
                        break
            case 3:
                break
            case _:
                print(Fore.RED + 'Erro! Opção inválida!')
    except ValueError:
        print(Fore.RED + 'Erro! digite algo válido.')
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário!")

print('Fim do programa!')

