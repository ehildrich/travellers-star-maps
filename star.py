
# Class Definitions
class Star: 
    def __init__(self, x: float, y: float, z: float, name: str, color: str, diameter: float):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.color = color
        self.diameter = diameter
    
    def __str__(self) -> str:
        return f"({self.name}, {self.x}, {self.y}, {self.z}, [{self.color}, {self.diameter}])"

class StarLine: 
    def __init__(self, firstStar: str, secondStar: str, color: str, diameter: float):
        self.firstStar = firstStar
        self.secondStar = secondStar
        self.color = color
        self.diameter = diameter
    
    def __str__(self) -> str:
        return f"({self.firstStar}, {self.secondStar}, [{self.color}, {self.diameter}])"

class StarInfo:
    def __init__(self, stars: set, lines: set): 
        self.stars = stars
        self.lines = lines
    