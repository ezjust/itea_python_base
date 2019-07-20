from users_manipulations import Users
from main_menu_class import MainMenu
import getpass
from colored_text import Colors

if __name__ == '__main__':
    pass

x = Users()
main_menu = MainMenu()
try:
    greetings = main_menu.print_asterisks(Colors.OKGREEN + "\
This is interactive menu of Neizbezhnost' football team" + Colors.ENDC)
    auth_reg = int(input("[1] to authorise\n[2] to register new user\nInput number: "))
except ValueError:
    print(Colors.FAIL + f'Wrong value inserted, try 1 or 2' + Colors.ENDC)
    exit(1)
if auth_reg == 1:
    auth_name = input('Input username to sign in: ')
    password = getpass.getpass("Input user's password: ")
    permissions_type = x.authorize_as(auth_name, password)
    if permissions_type:
        main_menu.manipulate_with_dict_functions(auth_name, permissions_type)
elif auth_reg == 2:
    name = input('Input new username:')
    password = getpass.getpass(f'Input password for {name} user:')
    x.register_new_user(name, password)
    if x.load_all_user_names()[name]:
        print(Colors.OKGREEN + f'User {name} successfully created, FYI all users get "user" minimal permissions\n\
to raise up permissions ask administrator' + Colors.ENDC)



