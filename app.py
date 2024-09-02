from helpers import *
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
        army_list = ListBuilder(faction, 1000)
        print("allowed unit types:", army_list.allowed_unit_types)
        print("current unit types:",army_list.current_unit_types)
       
        # Add a header for the list builder
        self.header_frame = Frame(self.window.root, pady=10)
        self.header_frame.pack(fill='x', pady=(10,5))
        
        #Label for the faction frame, aligned to the left
        faction_label = Label(
            self.header_frame, 
            text=f"Faction: {faction.name}", 
            font=("Helvetica", 12, "bold"))
        faction_label.pack(side='left', padx=(10, 0))
        
        #Frame for unit types status
        self.unit_status_frame = Frame(self.header_frame)
        self.unit_status_frame.pack(side='left', expand=True)
        
        # Create a frame and label for each unit type and store them in the App class
        self.commander_frame = Frame(self.unit_status_frame)
        self.commander_frame.pack(side='left', padx=5)

        self.commander_label = Label(
            self.commander_frame,
            text=f"Commander: {army_list.current_unit_types['Commander']}/{army_list.allowed_unit_types['Commander']['min']}-{army_list.allowed_unit_types['Commander']['max']}",
            font=("Helvetica", 10)
        )
        self.commander_label.pack()

        self.operative_frame = Frame(self.unit_status_frame)
        self.operative_frame.pack(side='left', padx=5)

        self.operative_label = Label(
            self.operative_frame,
            text=f"Operative: {army_list.current_unit_types['Operative']}/{army_list.allowed_unit_types['Operative']['min']}-{army_list.allowed_unit_types['Operative']['max']}",
            font=("Helvetica", 10)
        )
        self.operative_label.pack()

        self.corps_frame = Frame(self.unit_status_frame)
        self.corps_frame.pack(side='left', padx=5)

        self.corps_label = Label(
            self.corps_frame,
            text=f"Corps: {army_list.current_unit_types['Corps']}/{army_list.allowed_unit_types['Corps']['min']}-{army_list.allowed_unit_types['Corps']['max']}",
            font=("Helvetica", 10)
        )
        self.corps_label.pack()

        self.special_forces_frame = Frame(self.unit_status_frame)
        self.special_forces_frame.pack(side='left', padx=5)

        self.special_forces_label = Label(
            self.special_forces_frame,
            text=f"Special Forces: {army_list.current_unit_types['Special Forces']}/{army_list.allowed_unit_types['Special Forces']['min']}-{army_list.allowed_unit_types['Special Forces']['max']}",
            font=("Helvetica", 10)
        )
        self.special_forces_label.pack()

        self.support_frame = Frame(self.unit_status_frame)
        self.support_frame.pack(side='left', padx=5)

        self.support_label = Label(
            self.support_frame,
            text=f"Support: {army_list.current_unit_types['Support']}/{army_list.allowed_unit_types['Support']['min']}-{army_list.allowed_unit_types['Support']['max']}",
            font=("Helvetica", 10)
        )
        self.support_label.pack()

        self.heavy_frame = Frame(self.unit_status_frame)
        self.heavy_frame.pack(side='left', padx=5)

        self.heavy_label = Label(
            self.heavy_frame,
            text=f"Heavy: {army_list.current_unit_types['Heavy']}/{army_list.allowed_unit_types['Heavy']['min']}-{army_list.allowed_unit_types['Heavy']['max']}",
            font=("Helvetica", 10)
        )
        self.heavy_label.pack()
        
        #Label for activations and points, aligned to the right
        self.points_status_label = Label(
            self.header_frame,
            text = f'Activations: {army_list.activations}, Points: {army_list.current_points}/1000',
            font=("Helvetica", 12)
        )
        self.points_status_label.pack(side='right', padx=(0,10))
        
        # Create and pack frames for each section
        self.available_units_frame = Frame(self.window.root, width=160)
        self.available_units_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        self.unit_details_frame = Frame(self.window.root)
        self.unit_details_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        self.selected_units_frame = Frame(self.window.root)
        self.selected_units_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
        
        # Add labels for each section
        Label(self.available_units_frame, text="Available units", font=("Helvetica", 14)).pack(pady=10)
        Label(self.unit_details_frame, text="Details", font=("Helvetica", 14)).pack(pady=10)
        Label(self.selected_units_frame, text="Selected units", font=("Helvetica", 14)).pack(pady=10)
        
        # Scrollable frame setup for available units
        self.available_units_canvas = Canvas(self.available_units_frame, height=400)
        self.available_units_canvas.pack(side='left', fill='both', expand=True)
        
        # Scrollable frame setup for selected units
        self.selected_units_canvas = Canvas(self.selected_units_frame, height=400)
        self.selected_units_canvas.pack(side='left', fill='both', expand=True)
        
        # Create a vertical scrollbar linked to the available canvas
        available_scrollbar = Scrollbar(
            self.available_units_frame, 
            orient="vertical", 
            command=self.available_units_canvas.yview
            )
        available_scrollbar.pack(side='right', fill='y')
        
        # Create a vertical scrollbar linked to the selected canvas
        selected_scrollbar = Scrollbar(
            self.selected_units_frame, 
            orient="vertical", 
            command=self.selected_units_canvas.yview
            )
        selected_scrollbar.pack(side='left', fill='y')
        
        # Create an available inner frame to hold the actual content
        self.available_inner_frame = Frame(self.available_units_canvas)
        self.available_inner_frame.bind(
            "<Configure>", 
            lambda e: self.available_units_canvas.configure(scrollregion=self.available_units_canvas.bbox("all"))
            )
        
        # Create a selected inner frame to hold the actual content
        self.selected_inner_frame = Frame(self.selected_units_canvas)
        self.selected_inner_frame.bind(
            "<Configure>", 
            lambda e: self.selected_units_canvas.configure(scrollregion=self.selected_units_canvas.bbox("all"))
            )
        
        # Create a window inside the canvas to contain the inner frame
        self.available_units_canvas.create_window((0,0), window=self.available_inner_frame, anchor='nw')
        self.selected_units_canvas.create_window((0,0), window=self.selected_inner_frame, anchor='nw')
        
        # Configure the canvas to use the scrollbar
        self.available_units_canvas.configure(yscrollcommand=available_scrollbar.set)    
        self.selected_units_canvas.configure(yscrollcommand=selected_scrollbar.set)    
        
        # Create and pack buttons for each unit
        for unit_name, unit_info in faction.available_units.items():
            unit_row_frame = Frame(self.available_inner_frame)
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
                text="+",
                command=lambda name=unit_name: self.add_unit_to_list(name, faction, army_list)
            )
            add_button.pack(side='right', pady=5)
            
            bind_mousewheel_to_widget(unit_row_frame, self.available_units_canvas)       
            
        bind_mousewheel_to_widget(self.available_units_canvas, self.available_units_canvas)
        bind_mousewheel_to_widget(self.available_inner_frame, self.available_units_canvas)
        
        bind_mousewheel_to_widget(self.selected_units_canvas, self.selected_units_canvas)
        bind_mousewheel_to_widget(self.selected_inner_frame, self.selected_units_canvas)
        
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
        points = unit_info['points']
        type = unit_info['unit_type'] 
        unique = unit_info['unique']
        upgrades = unit_info['available_upgrades']   
           
        new_unit = Unit(unit_name, points, type, upgrades, unique) 
        if new_unit.unique == 0 or new_unit not in army.selected_units:         
            army.add_unit(new_unit)   
            
            print("current points:", army.current_points)
            
            # Frame to hold the unit label and the remove button on the same row
            unit_frame = Frame(self.selected_inner_frame)
            unit_frame.pack(pady=10, fill='x')        
            
            # Frame to hold the label and remove button side by side
            unit_row_frame = Frame(unit_frame)
            unit_row_frame.pack(fill='x') 
            
            selected_unit_label = Label(unit_row_frame, text=f"{unit_name} {unit_info['points']}p", font=("Helvetica", 12, "bold"))
            selected_unit_label.pack(side='left', anchor='w')
            
            # Add a remove button aligned to the right
            remove_button = Button(
                unit_row_frame,
                text='-',
                command=lambda: (
                    army.remove_unit(new_unit), 
                    unit_frame.destroy(), 
                    self.update_current_unit_types(army, type), 
                    self.update_points_status(army, self.points_status_label)
                    ),
                padx=5, pady=5
            )
            remove_button.pack(side='right')

            # Frame to hold the upgrade type buttons
            upgrade_types_frame = Frame(unit_frame)
            upgrade_types_frame.pack(pady=5, fill='x')     
            
            # Frame to hold the upgrade buttons
            upgrade_buttons_frame = Frame(unit_frame)
            upgrade_buttons_frame.pack(pady=5, fill='x')  
            
            bind_mousewheel_to_widget(unit_frame, self.selected_units_canvas)
            
            buttons_per_row = 4
            button_count = 0
            
            # Initial row frame
            current_row_frame = Frame(upgrade_types_frame)
            current_row_frame.pack(fill='x')
            
            for upgrade_type in upgrades:
                if button_count % buttons_per_row == 0 and button_count != 0:
                    current_row_frame = Frame(upgrade_types_frame)
                    current_row_frame.pack(fill='x')
                    
                upgrade_type_button = Button(
                    current_row_frame,
                    text=upgrade_type,
                    command=lambda u_type=upgrade_type: self.select_upgrade(new_unit, u_type, upgrade_buttons_frame, army),
                    padx=5, pady=2
                )
                upgrade_type_button.pack(side='left', padx=5, pady=5)
                
                button_count += 1
                
            # Updating unit type tracker, points and activations
            self.update_current_unit_types(army, type)
            self.update_points_status(army, self.points_status_label)
    
        
    def select_upgrade(self, unit, upgrade_type, parent_frame, army):        
        # Clear any existing upgrades in the upgrade_buttons_frame
        for frame in self.selected_inner_frame.winfo_children(): # unit_frame            
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
            
            bind_mousewheel_to_widget(upgrade_row_frame, self.selected_units_canvas)
            
            upgrade_button = Button(
                upgrade_row_frame,
                text=upgrade_name,
                command=lambda u_name=upgrade_name, u_value=upgrade_value: self.show_upgrade_details(u_name, u_value),                
            )
            upgrade_button.pack(side='left', padx=(0,5), pady=5)
            
            # Upgrade should be visually added, only if the upgrade slot is empty
            def add_upgrade_to_list_conditional(upgrade_name, upgrade_value):
                for slot in unit.upgrade_slots:
                    if slot['upgrade'] is not None and slot['upgrade'].name == upgrade_name:
                        return
                           
                for slot in unit.upgrade_slots:
                    if slot['type'] == upgrade_type and slot['upgrade'] is None:
                        print("upgrade being added to gui")
                        self.add_upgrade_to_list(upgrade_name, upgrade_value, upgrade_type, unit, army)                        
                        return
            
            add_button = Button(
                upgrade_row_frame,
                text='+',
                command=lambda u_name=upgrade_name, u_value=upgrade_value: (
                    add_upgrade_to_list_conditional(u_name, u_value), 
                    unit.add_upgrade(u_name, u_value, upgrade_type, army),
                    self.update_points_status(army, self.points_status_label)
                    )
            )
            add_button.pack(side='right', pady=5)            
        
    def add_upgrade_to_list(self, upgrade_name, upgrade_value, upgrade_type, unit, army):
        print(f"{upgrade_name} upgrade being added to list, for unit {unit.name}")
        for frame in self.selected_inner_frame.winfo_children():
            unit_row_frame = frame.winfo_children()[0]
            
            for index, child_frame in enumerate(unit_row_frame.winfo_children()):
                if isinstance(child_frame, Label) and unit.name in child_frame.cget('text'):
                    child_frame.config(text=f"{unit.name} {unit.points + upgrade_value['points']}p")  
                    upgrade_frame = Frame(frame)
                    
                    upgrade_button = Button(
                        upgrade_frame,
                        text=upgrade_name,
                        command=lambda: self.show_upgrade_details(upgrade_name, upgrade_value),
                        padx=5, pady=5
                    )
                    upgrade_button.pack(side='left', padx=(0,5), pady=5)
                    
                    def remove_update_visual(cf=child_frame):
                        cf.config(text=f"{unit.name} {unit.points - upgrade_value['points']}p")                        
                        upgrade_frame.destroy()
                    
                    remove_button = Button(
                        upgrade_frame,
                        text='-',
                        command=lambda: (
                            remove_update_visual(),
                            unit.remove_upgrade(upgrade_name, upgrade_type, army),
                            self.update_points_status(army, self.points_status_label)
                            ),
                        padx=5, pady=5
                    )
                    remove_button.pack(side='right', padx=(0,5), pady=5)
                    
                    if len(frame.winfo_children()) > 1:
                        upgrade_frame.pack(before=frame.winfo_children()[1], pady=5, fill='x')
                    else:
                        upgrade_frame.pack(pady=5, fill='x') 
                    return     
       
    def show_upgrade_details(self, name, value):
        widgets = self.unit_details_frame.winfo_children()        
        for index in range (1, len(widgets)):
            widgets[index].destroy()  
        
        details_label = Label(
            self.unit_details_frame, 
            text=f"Upgrade name: {name}\n Points: {value['points']}"
            )
        details_label.pack(pady=10)
        
        
    def update_current_unit_types(self, army, unit_type):
        #Construct the attribute name for the label dynamically
        label_name = f"{unit_type.lower()}_label"
        
        #Fetch the corresponding label object
        label = getattr(self, label_name, None)
        
        if label:
            current_count = army.current_unit_types[unit_type]  
            min_count = army.allowed_unit_types[unit_type]['min']
            max_count = army.allowed_unit_types[unit_type]['max']
            
            if current_count < min_count or current_count > max_count:
                color = "red"
            else:
                color = "black"
            label.config(
                text=f"{unit_type}: {current_count}/{min_count}-{max_count}",
                fg=color
            )
            
    def update_points_status(self, army, label):
        if army.current_points > army.max_points:
            color = "red"
        else:
            color = "black"
        
        label.config(
            text=f'Activations: {army.activations}, Points: {army.current_points}/1000',
            fg=color
        )
        
        print(f"Updating points to: {army.current_points}")

    def run(self):
        self.window.start()