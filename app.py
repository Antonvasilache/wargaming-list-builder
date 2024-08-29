from unit import Unit
from window import Window
from faction import Faction
from listBuilder import ListBuilder
from tkinter import Label, Frame, Button, Canvas, Scrollbar
import json


class App:
    def __init__(self, data_file='game_data.json'):        
        self.faction_names = ["Rebels", "Empire", "Republic", "CIS", "Mercenaries"]
        self.factions = {name: Faction(name) for name in self.faction_names}
        self.window = Window(width=1280, height=1024)
        self.data = self.load_game_data(data_file)
        self.setup_start_menu()
        
    def load_game_data(self, file_path):        
        with open(file_path, 'r') as file:
            return json.load(file)   
        
    def setup_start_menu(self):
        self.window.add_label("Select your faction: ")
        
        for faction_name in self.faction_names:
            self.window.add_button(faction_name, command=lambda name=faction_name: self.select_faction(name))
            
    
    def select_faction(self, faction_name):
        selected_faction = self.factions[faction_name].name
        print(selected_faction)
                
        self.window.clear_widgets()        
        
        self.setup_list_builder(selected_faction)
        
    def setup_list_builder(self, selected_faction):  
        faction = Faction(selected_faction)
        army_list = ListBuilder(faction, 800)
       
        # Add a label for the list builder
        self.window.add_label("Select your units:") 
        
        # Create and pack frames for each section
        self.available_units_frame = Frame(self.window.root, width=160)
        self.available_units_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        self.unit_details_frame = Frame(self.window.root)
        self.unit_details_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        self.selected_units_frame = Frame(self.window.root)
        self.selected_units_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        # Add labels for each section
        Label(self.available_units_frame, text="Available units", font=("Helvetica", 14)).pack(pady=10)
        Label(self.unit_details_frame, text="Unit details", font=("Helvetica", 14)).pack(pady=10)
        Label(self.selected_units_frame, text="Selected units", font=("Helvetica", 14)).pack(pady=10)
        
        # Scrollable frame setup for available units
        available_units_canvas = Canvas(self.available_units_frame, height=400)
        available_units_canvas.pack(side='left', fill='both', expand=True)
        
        # Create a vertical scrollbar linked to the canvas
        scrollbar = Scrollbar(
            self.available_units_frame, 
            orient="vertical", 
            command=available_units_canvas.yview
            )
        scrollbar.pack(side='right', fill='y')
        
        # Create an inner frame to hold the actual content
        inner_frame = Frame(available_units_canvas)
        inner_frame.bind(
            "<Configure>", 
            lambda e: available_units_canvas.configure(scrollregion=available_units_canvas.bbox("all"))
            )
        
        # Create a window inside the canvas to contain the inner frame
        available_units_canvas.create_window((0,0), window=inner_frame, anchor='nw')
        
        # Configure the canvas to use the scrollbar
        available_units_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Enable mouse wheel scrolling
        def on_mouse_wheel(event):
            if event.delta:
                available_units_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            else:
                if event.num == 4:
                    available_units_canvas.yview_scroll(-1, "units")
                elif event.num == 5:
                    available_units_canvas.yview_scroll(1, "units")
                    
        available_units_canvas.bind_all("<MouseWheel>", on_mouse_wheel)
        available_units_canvas.bind_all("<Button-4>", on_mouse_wheel)
        available_units_canvas.bind_all("<Button-5>", on_mouse_wheel)
        
        
        # Create and pack buttons for each unit
        for unit_name, unit_info in faction.available_units.items():
            unit_row_frame = Frame(inner_frame)
            unit_row_frame.pack(fill='x', pady=5)
            
            unit_text = f"{unit_name} ({unit_info['unit_type']})"
            points_text = f"{unit_info['points']}p"
            
            max_length = 35
            
            formatted_text = f"{unit_text:<{max_length - len(points_text)}}{points_text:>{len(points_text)}}"
            
            unit_button = Button(
                unit_row_frame, 
                text=formatted_text,
                command=lambda name=unit_name: self.show_unit_details(name, faction),
                width=45
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
        unit_info = faction.available_units[unit_name]
        
        unit_frame = Frame(self.selected_units_frame)
        unit_frame.pack(pady=10, fill='x')        
        
        selected_unit_label = Label(unit_frame, text=f"{unit_name} {unit_info['points']}p", font=("Helvetica", 12, "bold"))
        selected_unit_label.pack(anchor='w')
        
        unit_info = faction.available_units[unit_name]
        points = unit_info['points']
        type = unit_info['unit_type'] 
        upgrades = unit_info['available_upgrades']       
        
        new_unit = Unit(unit_name, points, type, upgrades)          
        army.add_unit(new_unit)     
        
        # Frame to hold the upgrade type buttons
        upgrade_types_frame = Frame(unit_frame)
        upgrade_types_frame.pack(pady=5, fill='x')     
        
        # Frame to hold the upgrade buttons
        upgrade_buttons_frame = Frame(unit_frame)
        upgrade_buttons_frame.pack(pady=5, fill='x')  
        
        for upgrade_type in upgrades:
            upgrade_type_button = Button(
                upgrade_types_frame,
                text=upgrade_type,
                command=lambda u_type=upgrade_type: self.select_upgrade(new_unit, u_type, upgrade_buttons_frame),
                padx=5, pady=2
                )
            upgrade_type_button.pack(side='left', padx=5, pady=5)
            
       
        
    def select_upgrade(self, unit, upgrade_type, parent_frame):        
        # Clear any existing upgrades in the upgrade_buttons_frame
        for frame in self.selected_units_frame.winfo_children(): # unit_frame            
            for child_frame in frame.winfo_children(): # upgrade_types_frame, upgrade_buttons_frame                
                if child_frame == parent_frame:
                    for widget in child_frame.winfo_children():
                        widget.destroy()   
            
        # Fetch the upgrades for the specific type from JSON data   
        upgrades = self.data['upgrade_cards']['type'][upgrade_type]   
        
        # Display available upgrades under the select unit's frame
        for upgrade_name, upgrade_value in upgrades.items():
            upgrade_row_frame = Frame(parent_frame)
            upgrade_row_frame.pack(fill='x', pady=5)
            
            upgrade_button = Button(
                upgrade_row_frame,
                text=upgrade_name,
                command=lambda u_name=upgrade_name, u_value=upgrade_value: self.show_upgrade_details(u_name, u_value),                
            )
            upgrade_button.pack(side='left', padx=(0,5), pady=5)
            
            # Upgrade should be visually added, only if the upgrade slot is empty
            def add_upgrade_to_list_conditional(upgrade_name, upgrade_value):                
                for slot in unit.upgrade_slots:
                    if slot['type'] == upgrade_type and slot['upgrade'] is None:
                        print("upgrade being added to gui")
                        self.add_upgrade_to_list(upgrade_name, upgrade_value, upgrade_type, unit)
                        return
            
            add_button = Button(
                upgrade_row_frame,
                text='Add',
                command=lambda u_name=upgrade_name, u_value=upgrade_value: (add_upgrade_to_list_conditional(u_name, u_value), unit.add_upgrade(u_name, u_value, upgrade_type))
            )
            add_button.pack(side='right', pady=5)            
        
    def add_upgrade_to_list(self, upgrade_name, upgrade_value, upgrade_type, unit):
        print(f"{upgrade_name} upgrade being added to list, for unit {unit.name}")
        for frame in self.selected_units_frame.winfo_children():
            for index, child_frame in enumerate(frame.winfo_children()):
                if isinstance(child_frame, Label) and unit.name in child_frame.cget('text'):
                    upgrade_frame = Frame(frame)
                    
                    upgrade_button = Button(
                        upgrade_frame,
                        text=upgrade_name,
                        command=lambda: self.show_upgrade_details(upgrade_name, upgrade_value),
                        padx=5, pady=5
                    )
                    upgrade_button.pack(side='left', padx=(0,5), pady=5)
                    
                    remove_button = Button(
                        upgrade_frame,
                        text='-',
                        command=lambda: (upgrade_frame.destroy(), unit.remove_upgrade(upgrade_name, upgrade_type)),
                        padx=5, pady=5
                    )
                    remove_button.pack(side='left', padx=(0,5), pady=5)
                    
                    if len(frame.winfo_children()) > index + 1:
                        upgrade_frame.pack(before=frame.winfo_children()[index+1], pady=5, fill='x')
                    else:
                        upgrade_frame.pack(pady=5, fill='x')                
                    
        
    def show_upgrade_details(self, name, value):
        widgets = self.unit_details_frame.winfo_children()        
        for index in range (1, len(widgets)):
            widgets[index].destroy()  
        
        details_label = Label(
            self.unit_details_frame, 
            text=f"Upgrade name: {name}\n Points: {value['points']}"
            )
        details_label.pack(pady=10)
            
         
    
    
    def run(self):
        self.window.start()