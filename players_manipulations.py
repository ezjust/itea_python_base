import json


class FootballPlayer:
    """This class initialise new players and their characteristics"""
    def __init__(self, name, age, strength, savvy, dribbling, player_pos, player_sal, player_con):
        self.name = name
        self.age = age
        self.skills = (strength, savvy, dribbling) # maximum 100
        self.details = {"position": player_pos, "salary": player_sal, "contract": player_con}


class PlayerManipulations(FootballPlayer):
    """This class helps to make manipulations with players"""

    # def show_player(self):
    #     read_json = json.dumps('players.json')
    #     if read_json:
    #         for line in read_json:

    def save_player(self):
        with open('players.json', 'w') as json_file:
            json.dump((self.name, self.age, self.skills, self.details), json_file)
    # def change_player(self):
    #
    # def remove_player(self):


x = FootballPlayer('EZ', 28, 80, 99, 50, 'DEF', 2500, '3 years')
y = PlayerManipulations('EZ', 28, 80, 99, 50, 'DEF', 2500, '3 years')
y.save_player()
