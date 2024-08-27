from faction import Faction
from listBuilder import ListBuilder
from window import Window
from tkinter import Label, Frame, Button


class App:
    def __init__(self):        
        self.faction_names = ["Rebels", "Empire", "Republic", "CIS", "Mercenaries"]
        self.factions = {name: Faction(name) for name in self.faction_names}
        self.window = Window(width=800, height=600)
        self.setup_start_menu()      
    
        
    def setup_start_menu(self):
        self.window.add_label("Select your faction: ")
        
        for faction_name in self.faction_names:
            self.window.add_button(faction_name, command=lambda name=faction_name: self.select_faction(name))
            
    
    def select_faction(self, faction_name):
        selected_faction = self.factions[faction_name].name
        print(selected_faction)
        # self.window.show_message("Faction Selected", f"You have selected: {selected_faction}")
        
        self.window.clear_widgets()
        #self.window.root.destroy()
        
        self.setup_list_builder(selected_faction)
        
    def setup_list_builder(self, selected_faction):  
        faction = Faction(selected_faction)
        army_list = ListBuilder(faction, 800)
        # print(faction.available_units)
        # Add a label for the list builder
        self.window.add_label("Select your units:")
        
        # Create and pack frames for each section
        self.available_units_frame = Frame(self.window.root, width=100)
        self.available_units_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        self.unit_details_frame = Frame(self.window.root)
        self.unit_details_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        self.selected_units_frame = Frame(self.window.root)
        self.selected_units_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        # Add labels for each section
        Label(self.available_units_frame, text="Available units", font=("Helvetica", 14)).pack(pady=10)
        Label(self.unit_details_frame, text="Unit details", font=("Helvetica", 14)).pack(pady=10)
        Label(self.selected_units_frame, text="Selected units", font=("Helvetica", 14)).pack(pady=10)
        
        # Create and pack buttons for each unit
        for unit_name, unit_info in faction.available_units.items():
            unit_row_frame = Frame(self.available_units_frame)
            unit_row_frame.pack(fill='x', pady=5)
            
            unit_button = Button(
                unit_row_frame, 
                text=f"{unit_name} ({unit_info['unit_type']})",
                command=lambda name=unit_name: self.show_unit_details(name, faction),
                width= 25
            )
            unit_button.pack(side='left', padx=(0,5), pady=5)
            
            add_button = Button(
                unit_row_frame,
                text="Add",
                command=lambda name=unit_name: self.add_unit_to_list(name, faction, army_list)
            )
            add_button.pack(side='right', pady=5)
        
        # Make sure the frames are visible
        self.available_units_frame.pack_propagate(False)
        self.unit_details_frame.pack_propagate(False)
        self.selected_units_frame.pack_propagate(False)

        
    def show_unit_details(self, unit_name, faction):
        widgets = self.unit_details_frame.winfo_children()        
        for index in range (1, len(widgets)):
            widgets[index].destroy()            
            
        unit_info = faction.available_units[unit_name]
        details_label = Label(
            self.unit_details_frame, 
            text=f"Unit: {unit_name}\nType: {unit_info['unit_type']}\n Points: {unit_info['points']}"
            )
        details_label.pack(pady=10)
    
    def add_unit_to_list(self, unit_name, faction, army):
        selected_unit_label = Label(self.selected_units_frame, text=unit_name)
        selected_unit_label.pack(pady=5)
        unit_info = faction.available_units[unit_name]
        army.add_unit({unit_name: unit_info})
        #army[unit_name] = unit_info
        print(army.selected_units)
        
        
        
    def run(self):
        self.window.start()