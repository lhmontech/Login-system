from colorama import init, Fore
import getpass

init(autoreset=True)

users = {'Admin':hash('123456'),'Lucas':hash('root')}
blocked = set()

while True:
    try:
        print('\nWelcome to lhmontech login system!\n 1- Sign-in\n 2- Sign-up\n 3- Quit')
        option = int(input('\nType what you want to do:'))
        match option:
            case 1:
                cont = 1
                while cont < 4:
                    user = input('\nEnter your username:')
                    if user in blocked:
                        print(Fore.RED + 'Blocked user!')
                        continue
                    elif cont > 3:
                        print(Fore.RED + 'Failed attempts')
                        break
                    elif user not in users:
                        print(Fore.RED + 'Invalid user!')
                        cont += 1
                    else:
                        conts = 1
                        while conts < 4:
                            senha = hash(getpass.getpass(prompt='\nEnter your password: '))
                            if conts > 3:
                                blocked.add(user)
                                print(Fore.RED + 'Failed attempts')
                                cont = 4
                                break
                            elif senha != users[user]:
                                print(Fore.RED + 'Invalid password!')
                                conts += 1
                            else:
                                print(Fore.BLUE + f'Successful login, welcome {user}!')
                                while True:
                                    option = int(input('\nSelect an option:\n'
                                                      ' 1- Registered users\n 2- Remove an user\n 3- Blocked users\n'
                                                      ' 4- Unlock an user\n 5- Quit\n '))
                                    match option:
                                        case 1:
                                            print('\nRegistered users list:')
                                            print(*users.keys(), sep='\n')
                                        case 2:
                                            user = input('\nEnter the username that you want to remove:')
                                            del users[user]
                                            print(Fore.BLUE + 'User removed!')
                                        case 3:
                                            print('\nBlocked users list:')
                                            print(*blocked, sep='\n')
                                        case 4:
                                            user = input('\nEnter the username that you want to unlock:')
                                            blocked.remove(user)
                                            print(Fore.BLUE + 'User unlocked!')
                                        case 5:
                                            break
                                        case _:
                                            print(Fore.RED + '\nSelect a valid option!')
                                cont = 4
                                break
            case 2:
                print('Registration area.')
                while True:
                    user = input('\nEnter an username: ')
                    if user in users:
                        print('\nUsername already in use!')
                    else:
                        users[user] = hash(getpass.getpass(prompt='\nDenter a password: '))
                        print(Fore.BLUE + '\nRegistration completed successfully!')
                        break
            case 3:
                break
            case _:
                print(Fore.RED + 'Error! invalid option!')
    except ValueError:
        print(Fore.RED + 'Error! Enter something valid!')
    except KeyboardInterrupt:
        print("Program stopped by user!")

print('End of the program!')
