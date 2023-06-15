class Character:
    name = ""
    steps = None
    position = None
    
    def __init__(self, character_name, character_steps, character_position):
        self.name = character_name
        self.steps = character_steps
        self.position = character_position