class Unit:
    def __init__(self, name, points, unit_type):
        self.name = name
        self.points = points
        self.unit_type = unit_type
        self.upgrade_slots = dict() # {Upgrade.type: filled}
        self.upgrades = list() # [Upgrade]
    
    def add_upgrade(self, upgrade):
        pass
        