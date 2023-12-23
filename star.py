
# Global Variables

COLORS = {
            "blue" : (51, 148, 255), 
            "brown" : (123, 68, 0), 
            "gray" : (50, 50, 50), 
            "green" : (25, 224, 25), 
            "orange" : (255, 121, 0), 
            "purple" : (106, 1, 250), 
            "red" : (214, 16, 16), 
            "white" : (255,255,255), 
            "yellow" : (249, 218, 2) 
}


# Class Definitions

# Defines the parameters of the board
class StarParameters:
    def __init__(self, imgSize, edgeSize, lineWidth, offset, starSize, circleSize, fontSize): 
        self.IMAGE_SIZE = int(imgSize) if int(imgSize) > 1 else 200
        self.RESOLUTION = self.IMAGE_SIZE/200
        self.EDGE_SIZE = int(edgeSize) if int(edgeSize) > 1 else 2
        self.LINE_WIDTH = int(lineWidth*4) if int(lineWidth*4) >= 1 else 4
        self.LINE_OFFSET = int(offset*4) if int(offset*4) >= 1 else 4
        self.MAX_STAR_SIZE = int(starSize*4) if int(starSize*4) >= 1 else 4
        self.CIRCLE_SIZE = int(circleSize*4) if int(circleSize*4) >= 1 else 4
        self.FONT_SIZE = int(fontSize*4) if int(fontSize*4) >= 1 else 4
        
        # The size of the circle is limited to the offset of the connecting 
        # lines to prevent the lines from overlapping the circles
        if (self.CIRCLE_SIZE / 2 > self.LINE_OFFSET): 
            self.CIRCLE_SIZE = self.LINE_OFFSET * 2 - self.LINE_WIDTH  

        # If the max star size is greater than the circle size, increase 
        # the circle size to be slightly larger than the max circle size
        if (self.MAX_STAR_SIZE > self.CIRCLE_SIZE): 
            self.CIRCLE_SIZE = self.MAX_STAR_SIZE + 1
        
        print(self.LINE_WIDTH)
    
# Defines a Star object
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

# Defines a line between two stars
class StarLine: 
    def __init__(self, firstStar: str, secondStar: str, color: str, diameter: float):
        self.firstStar = firstStar
        self.secondStar = secondStar
        self.color = color
        self.diameter = diameter
    
    def __str__(self) -> str:
        return f"({self.firstStar}, {self.secondStar}, [{self.color}, {self.diameter}])"

# Defines all of the information about a board, including 
# all of its stars and the lines between them
class StarInfo:
    def __init__(self, stars: set, lines: set, params: StarParameters): 
        self.stars = stars
        self.lines = lines
        self.params = params
    