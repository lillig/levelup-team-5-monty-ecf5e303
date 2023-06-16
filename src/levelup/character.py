from levelup.position import Position

class Character:
    name = ""
    steps = None
    position = None
    map = None

    def __init__(self, character_name, character_steps, character_position, character_map=None):
        self.name = character_name
        self.steps = character_steps
        self.position = character_position
        self.map = character_map
    
    def move(self, direction):
        new_coordinates = self.calculatePosition(direction, self.position.coordinates)
        self.position = Position(new_coordinates)

    def calculatePosition(self, direction, current_position):
        return self.map.calculatePosition(direction, current_position)