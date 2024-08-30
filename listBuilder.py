import json

class ListBuilder:
    def __init__(self, faction, max_points):
        self.faction = faction
        self.max_points = max_points
        self.selected_units = list()
        self.current_points = 0
        self.allowed_unit_types = {} 
        self.current_unit_types = {}
        self.command_cards = {} # {type: qty_required}
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
    
    def save_list(self, filename):
        pass
    
    def load_list(self, filename):
        pass
    
    def clear_list(self):
        # add 'are you sure' message
        pass
    
    
    