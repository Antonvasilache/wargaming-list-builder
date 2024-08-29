class Upgrade:
    def __init__(self, name, points, type):
        self.name = name
        self.points = points
        self.type = type
        
    def __repr__(self):
        return f"{self.name}: {self.points}"