import json
import pickle
import os
from tkinter import simpledialog

class ListBuilder:
    def __init__(self, faction, max_points):
        self.faction = faction
        self.max_points = max_points
        self.selected_units = list()
        self.current_points = 0
        self.allowed_unit_types = {} 
        self.current_unit_types = {}
        self.command_cards = {} 
        self.activations = 0
        
        self.load_unit_types()  
        
    def load_unit_types(self):
        with open('unit_limits.json', 'r') as file:
            unit_limits = json.load(file)
            
        if self.max_points == 1000:
            self.allowed_unit_types = unit_limits['Standard']
        elif self.max_points == 1600:
            self.allowed_unit_types = unit_limits['Grand']
            
        self.current_unit_types = {unit_type: 0 for unit_type in self.allowed_unit_types.keys()}
        
    def add_unit(self, unit):        
        if unit.unique == 0 or unit not in self.selected_units:
            self.selected_units.append(unit)
            self.activations += 1
            self.current_points += unit.points
            self.current_unit_types[unit.unit_type] += 1 
        else:
            print("Unique unit can only be added once")
    
    def remove_unit(self, unit):
        self.selected_units.remove(unit)
        self.activations -= 1
        self.current_points -= unit.points
        self.current_unit_types[unit.unit_type] -= 1
    
    def add_command_card(self, command_card):
        pass
    
    def remove_command_card(self, command_card):
        pass
    
    def save_list(self):
        list_name = simpledialog.askstring("Save army list", "Enter the name of your army:")
        
        if not list_name:
            return
        
        current_directory = os.path.join(os.getcwd(), "saved lists")
        filename = f"{list_name}.pkl"        
        file_path = os.path.join(current_directory, filename)
        
        os.makedirs(current_directory, exist_ok=True)
        
        try:
            with open(file_path, 'wb') as file:
                pickle.dump(self, file)
            print(f"List saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving list: {e}")
            
    
    # def load_list(self, filename):
    #     try:
    #         with open(filename, 'rb') as file:
    #             army_list = pickle.load(file)
    #         print(f"List loaded successfully from {filename}")
    #         return army_list
    #     except Exception as e:
    #         print(f"error loading list: {e}")
    #         return None
    
    def clear_list(self):
        # add 'are you sure' message
        pass
    
    def __repr__(self):
        return self.faction.name
    
    
    