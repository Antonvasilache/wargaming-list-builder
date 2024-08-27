class ListBuilder:
    def __init__(self, faction, max_points):
        self.faction = faction
        self.max_points = max_points
        self.selected_units = list() # [Unit]
        self.current_points = 0
        self.unit_types = {} # {unit_type: max_allowed}
        self.command_cards = {} # {type: qty_required}
        self.activations = 0   
        
    def add_unit(self, unit):
        self.selected_units.append(unit)
    
    def remove_unit(self, unit):
        pass
    
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
    