class Map:
    height = None
    width = None
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def calculatePosition(self, direction, coordinates):
        match direction:
            case 'N':
                coordinates = (coordinates[0], coordinates[1] - 1)
            case 'S':
                coordinates = (coordinates[0], coordinates[1] + 1)
            case 'E':
                coordinates = (coordinates[0] + 1, coordinates[1])
            case 'W':
                coordinates = (coordinates[0] - 1, coordinates[1])
        return self.validatePosition(coordinates)

    def validatePosition(self, coordinates):
        if coordinates[1]==-1:
            coordinates = (coordinates[0], 0)
        elif coordinates[0]==-1:
            coordinates = (0, coordinates[1])
        elif coordinates[0]==10:
            coordinates = (9, coordinates[1])
        elif coordinates[1]==10:
            coordinates = (coordinates[0], 9)
        return coordinates