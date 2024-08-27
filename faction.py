import json

class Faction:
    def __init__(self, name, data_file='game_data.json'):
        self.data = self.load_game_data(data_file)
        self.name = name
        self.available_units = self.data['factions'][name]['units'] # [Unit]
        self.available_command_Cards = list() # [CommandCard]
        
    def load_game_data(self, file_path):        
        with open(file_path, 'r') as file:
            return json.load(file)
    
    def filter_by_unit_type(self, unit_type):
        pass