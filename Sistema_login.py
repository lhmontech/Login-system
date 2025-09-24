from colorama import init, Fore

init(autoreset=True)

usuarios = {'Admin':hash('123456'),'Lucas':hash('abcd'),'Pablo':hash('escobar')}
bloqueados = set()

while True:
    try:
        print('\nBem vindo ao sistema de login lhmontech!\n 1- Entrar\n 2- Cadastro\n 3- Sair')
        opcao = int(input('\nDigite o que gostaria de fazer:'))
        match opcao:
            case 1:
                cont = 1
                while cont <= 3:
                    usuario = input('\nDigite o seu nome de usuário:')
                    if usuario in bloqueados:
                        print(Fore.RED + 'Usuário bloqueado!')
                        continue
                    elif cont == 3:
                        print(Fore.RED + 'Tentativas esgotadas!')
                        break
                    elif usuario not in usuarios:
                        print(Fore.RED + 'Usuário inválido!')
                        cont += 1
                    else:
                        conts = 1
                        while conts <= 3:
                            senha = hash(input('\nDigite sua senha: '))
                            if conts == 3:
                                bloqueados.add(usuario)
                                print(Fore.RED + 'Tentativas esgotadas!')
                                cont = 4
                                break
                            elif senha != usuarios[usuario]:
                                print(Fore.RED + 'Senha inválida!')
                                conts += 1
                            else:
                                print(Fore.BLUE + 'Bem vindo!')
                                while True:
                                    opcao = int(input('\nSelecione uma opção:\n'
                                                      ' 1- Usuários cadastrados\n 2- Remover usuário\n 3- Usuários bloqueados\n'
                                                      ' 4- Desbloquear usuário\n 5- Sair\n '))
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
                                cont = 4
                                break
            case 2:
                print('Área de cadastro.')
                while True:
                    usuario = input('\nDigite o nome do usuario: ')
                    if usuario in usuarios:
                        print('\nNome de usuário já em uso!')
                    else:
                        usuarios[usuario] = hash(input('Digite a senha: '))
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
