from upgrade import Upgrade

class Unit:
    def __init__(self, name, points, unit_type, upgrades):
        self.name = name
        self.points = points
        self.unit_type = unit_type
        self.available_upgrades = upgrades
        self.upgrade_slots = [
            {'type': upgrade_type, 'upgrade': None}
            for upgrade_type in self.available_upgrades]
        
        
    def __repr__(self):
        return (f"Unit(name='{self.name}', points={self.points}, "
                f"unit_type='{self.unit_type}', available upgrades={self.available_upgrades}, upgrade slots={self.upgrade_slots})")
        
    def add_upgrade(self, name, value, type):   
        for slot in self.upgrade_slots:
            if slot['type'] == type and slot['upgrade'] is None:     
                upgrade = Upgrade(name, value['points'], type)
                slot['upgrade'] = upgrade
                print(self.upgrade_slots)
                print('upgrade added successfully')
                return
        print(f"No available slot for upgrade type {type}")
            
    def remove_upgrade(self, name, type):
        for slot in self.upgrade_slots:            
            if (
                slot['type'] == type 
                and slot['upgrade'] is not None 
                and slot['upgrade'].name == name):
                slot['upgrade'] = None                       
                print(self.upgrade_slots)
                print('upgrade removed successfully')
                return
            
        print("No upgrade found to remove")
        
        