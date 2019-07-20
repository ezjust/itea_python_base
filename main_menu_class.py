from users_manipulations import Users
from players_manipulations_by_classes import PlayerManipulations
from players_manipulations_by_classes import FootballPlayer
from colored_text import Colors


class MainMenu:

    def print_asterisks(self, words):  # function for asterisks printing
        asterisks_len = '*' * (len(words) - 5)
        print(asterisks_len)
        print(f'* {words} *')
        print(asterisks_len)

    def manipulate_with_dict_functions(self, login_name, permission_type):
        count = 1
        all_fields = ('age (years)', 'strength (max 100)', 'savvy (max 100)', 'dribbling (max 100)', 'player position',
                      'player salary per day (max 100$)', 'player contract (years)')
        print(f'\nHello {login_name}, What do you want to do?')
        dict_of_functions = {'User Manipulations:': ('change password', 'change user permissions', 'block user'),
                             'Data Manipulations:': ('add new player', 'change player info', 'remove player',
                                                     'show team player')}
        if permission_type == 'user':
            for key, value in dict_of_functions.items():
                for v in value:
                    if v == 'show team players':
                        print(f'{key}\n {count}){v}')
            choice = int(input(f"\nYou could only view player's info.Please input '{count}' and press Enter: "))
            if choice == count:
                player_name = str(input(f'Which player info you want to get? Insert name: '))
                x = PlayerManipulations()
                x.show_player(player_name)
            else:
                raise ValueError(Colors.WARNING + f"you've inserted wrong value, \
it could be inserted only '{count}'" + Colors.ENDC)
                exit()
        elif permission_type == 'half_admin':
            for key, value in dict_of_functions.items():
                if key == 'Data Manipulations:':
                    print(f'\n{key}')
                    print(f'\t{count}){value[0]}\n\t{count+1}){value[3]}')
            choice = int(input(f'Please input "{count}" or "{count+1}" and press Enter: '))
            if choice == count:
                user_name = input('Insert name new of player:')
                options = []
                for option in all_fields:
                    new_option = input(f'Insert {option} of new player: ')
                    if new_option.isdigit():
                        if int(new_option) in range(0, 101):
                            options.append(new_option)
                    elif isinstance(new_option, str):
                        if len(str(new_option)) <= 30:
                            options.append(new_option)
                    else:
                        raise ValueError
                        exit(1)
                options.insert(0, user_name)
                x = PlayerManipulations(*options)
                x.save_player()
                print(Colors.OKGREEN + f'Player {user_name} saved successfully' + Colors.ENDC)
            elif choice == (count+1):
                player_name = input(f'\nWhich player info you want to get? Insert name: ')
                x = PlayerManipulations()
                x.show_player(player_name)
            else:
                raise ValueError(Colors.WARNING + f"you've inserted wrong value \
it could be inserted only '{count}'" + Colors.ENDC)
                exit()
        elif permission_type == 'administrator':
            for key, value in dict_of_functions.items():
                print(f'\n{key}')
                for v in value:
                    print(f'\t{count}){v}')
                    count += 1
            choice = int(input(f'\nPlease choose option and press Enter: '))
            if choice == 1:
                user_name = input('Insert name of user:')
                new_password = input('Insert new password')
                x = Users()
                x.change_password(user_name, new_password)
            elif choice == 2:
                user_name = input('Insert name of user:')
                new_perms = input('Input new role (user, half_admin or administrator):')
                x = Users()
                x.change_permissions(user_name, new_perms)
                print(f'{user_name} get new permissions {new_perms}')
            elif choice == 3:
                user_name = input('Insert name of user: ')
                answer = input(f'\nDo you want to block this {user_name} user? Insert "yes" or "no": ')
                if answer == 'yes':
                    x = Users()
                    x.change_permissions(user_name, 'blocked')
                    print(f'{user_name} user blocked')
                elif answer == 'no':
                    print(f'Lucky {user_name} is not blocked yet')
                else:
                    print('Wrong input')
            elif choice == 4:
                options = []
                user_name = input('Insert name new of player: ')
                for option in all_fields:
                    new_option = input(f'Insert {option} of new player: ')
                    if new_option.isdigit():
                        if int(new_option) in range(0, 101):
                            options.append(new_option)
                    elif isinstance(new_option, str):
                        if len(str(new_option)) <= 30:
                            options.append(new_option)
                    else:
                        raise ValueError
                        exit(1)
                options.insert(0, user_name)
                x = PlayerManipulations(*options)
                x.save_player()
                print(Colors.OKGREEN + f'Player {user_name} saved successfully' + Colors.ENDC)
            elif choice == 5:
                options = []
                user_name = input('Insert name of player: ')
                for option in all_fields:
                    new_option = input(f'Insert {option} of new player: ')
                    if new_option.isdigit():
                        if int(new_option) in range(0, 101):
                            options.append(new_option)
                    elif isinstance(new_option, str):
                        if len(str(new_option)) <= 30:
                            options.append(new_option)
                    else:
                        raise ValueError
                        exit(1)
                options.insert(0, user_name)
                FootballPlayer(*options)
                x = PlayerManipulations()
                x.change_player(user_name)
                print(Colors.OKGREEN + f'Player {user_name} saved successfully' + Colors.ENDC)
            elif choice == 6:
                user_name = input('Insert name of player to remove:')
                x = PlayerManipulations()
                x.remove_player(user_name)
            elif choice == 7:
                player_name = input(f'Which player info you want to get? insert name:')
                x = PlayerManipulations()
                x.show_player(player_name)
            else:
                print(Colors.WARNING + 'Wrong value input' + Colors.ENDC)
        else:
            print(Colors.WARNING + 'Ohh, your user is blocked, ask administrator to make unblock' + Colors.ENDC)
