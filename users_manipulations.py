import pickle
from exceptions import NoUser
from colored_text import Colors

class Users:

    def __init__(self):
        self.possible_perms = ('user', 'half_admin', 'administrator', 'blocked')

    def load_all_user_names(self):
        with open('users.pickle', 'rb') as f:
            users = pickle.load(f)
        return users

    def default_admin(self):
        try:
            self.load_all_user_names()
        except EOFError:
            with open('users.pickle', 'wb') as f:
                pickle.dump({'admin': ('administrator', 123456)}, f)

    def save_to_pickle(self, users_update):
        with open('users.pickle', 'wb') as f:
            pickle.dump(users_update, f)

    def register_new_user(self, name, password):
        self.password = password
        self.default_admin()
        users = self.load_all_user_names()
        users[name] = ('user', f'{password}')
        self.save_to_pickle(users)

    def authorize_as(self, name, password):
        self.default_admin()
        users = self.load_all_user_names()
        try:
            int(password) == users[name][1]
            try:
                user_permissions = (users[name][0])
                return user_permissions
            except KeyError:
                print(Colors.FAIL + f'There is no "{name}" user registered yet' + Colors.ENDC)
                exit()
        except ValueError:
            print(Colors.FAIL + 'Wrong password inserted, please try again' + Colors.ENDC)

    def change_permissions(self, name, new_permission):
        self.default_admin()
        users = self.load_all_user_names()
        if users[name]:
            try:
                if new_permission in self.possible_perms:
                    password = (users[name][1])
                    users[name] = (f'{new_permission}', f'{password}')
                    self.save_to_pickle(users)
            except KeyError:
                print(Colors.WARNING + f'there is no such {new_permission} permission type' + Colors.ENDC)
                exit()
        else:
            raise NoUser(Colors.FAIL + 'There is no "{name}" user registered yet' + Colors.ENDC)
            exit()

    def change_password(self, name, password):
        self.default_admin()
        users = self.load_all_user_names()
        try:
            users[name]
            permissions = (users[name][0])
            users[name] = (f'{permissions}', f'{password}')
            self.save_to_pickle(users)
        except KeyError:
            print(Colors.WARNING + f'There is no "{name}" user registered yet' + Colors.ENDC)
            exit()
