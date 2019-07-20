import json
from colored_text import Colors


class FootballPlayer:
    """This class initialise new players and their characteristics"""
    def __init__(self, name=None, age=None, strength=None, savvy=None, dribbling=None, player_pos=None, player_sal=None, player_con=None):
        self.name = name
        self.age = age
        self.skills = (strength, savvy, dribbling)  # maximum 100
        self.details = {"Position": player_pos, "Salary": player_sal, "Contract years": player_con}


class FileManipulations:
    def read_file(self):
        with open('players.json', 'r') as json_file:
            player_dict = json.load(json_file)
        return player_dict

    def write_to_file(self, player_dict):
        with open('players.json', 'w') as json_file:
            json.dump(player_dict, json_file)


class PlayerManipulations(FootballPlayer, FileManipulations):
    """This class helps to make manipulations with players"""

    def show_player(self, name):
        try:
            self.read_file()[name]
            print(f'Player: {name}')
            for key, value in self.read_file()[name].items():
                if isinstance(value, int):
                    print(f'{key}: {value}')
                elif isinstance(value, str):
                    print(f'{key}: {value}')
                elif isinstance(value, list):
                    skills = ('strength', 'savvy', 'dribbling')
                    print(f'{key}:')
                    for s, v in zip(skills, value):
                        print(f'\t{s} - {v}')
                else:
                    for dict_key, dict_value in value.items():
                        print(f'{dict_key}: {dict_value}')
        except KeyError:
            print(Colors.WARNING + f'No player with name "{name}" in team list' + Colors.ENDC)

    def save_player(self):
        with open('players.json', 'r') as json_read:
            if not json_read.read():
                player_dict = {f'{self.name}': {"Age": self.age, "Skills": self.skills, "Details": self.details}}
            else:
                player_dict = self.read_file()
                player_dict[f'{self.name}'] = {"Age": self.age, "Skills": self.skills, "Details": self.details}
        self.write_to_file(player_dict)

    def change_player(self, name):
        player_dict = self.read_file()
        player_dict[name] = {"Age": self.age, "Skills": self.skills, "Details": self.details}
        self.write_to_file(player_dict)

    def remove_player(self, name):
        try:
            self.read_file()[name]
            player_dict = self.read_file()
            answer = str(input(Colors.WARNING + f'Are you sure you want to delete "{name}" player from the team list? \
\nType "yes" or "no":' + Colors.ENDC))
            if answer == 'yes':
                del player_dict[name]
                self.write_to_file(player_dict)
                print(Colors.OKGREEN + f'Player "{name}" has been deleted' + Colors.ENDC)
            elif answer == 'no':
                print(Colors.WARNING + 'No changes in team list' + Colors.ENDC)
            else:
                print(Colors.WARNING + 'Wrong answer, print only "yes" or "no" next time' + Colors.ENDC)
        except KeyError:
            print(Colors.FAIL + f'No player with name "{name}" in team list' + Colors.ENDC)
