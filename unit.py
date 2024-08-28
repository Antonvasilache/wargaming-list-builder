class Unit:
    def __init__(self, name, points, unit_type, upgrades):
        self.name = name
        self.points = points
        self.unit_type = unit_type
        self.available_upgrades = upgrades
        self.upgrade_slots = {upgrade_type: None for upgrade_type in self.available_upgrades}
        
        
    def __repr__(self):
        return (f"Unit(name='{self.name}', points={self.points}, "
                f"unit_type='{self.unit_type}', available upgrades={self.available_upgrades}, upgrade slots={self.upgrade_slots})")
        
    def add_upgrade(self, upgrade, upgrade_cards):
        if upgrade not in upgrade_cards:
            print(f"Upgrade {upgrade} not found in upgrade cards")
            return
        
        upgrade_info = upgrade_cards[upgrade]
        upgrade_type = upgrade_info['type']
        
        if upgrade_type not in self.upgrade_slots:
            print(f"Upgrade type {upgrade_type} is not available for this unit.")
            return
        
        if self.upgrade_slots[upgrade_type] is not None:
            print(f"Upgrade slot for type {upgrade_type} is already occupied by {self.upgrade_slots[upgrade_type]}")
            return
        
        self.upgrade_slots[upgrade_type] = upgrade
        print(f"Added upgrade {upgrade} to {self.name} in slot {upgrade_type}")
        
        
        