import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

# Global Variables
IMAGE_SIZE = 800
EDGE_SIZE = 20
STAR_SIZE = 8



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



# Function Definitions

# Draws the gridlines at the edges of the board and the centerlines that pass through the middle of board
def drawEdgeRule(draw): 
    # Start with center lines
    draw.line([(0, EDGE_SIZE + (IMAGE_SIZE/2)), (IMAGE_SIZE + EDGE_SIZE*2, EDGE_SIZE + (IMAGE_SIZE/2))], (50,50,50), 1)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE/2), 0), (EDGE_SIZE + (IMAGE_SIZE/2), IMAGE_SIZE + EDGE_SIZE*2)], (50,50,50), 1)

    #Draw map edges
    draw.line([(0, EDGE_SIZE), (IMAGE_SIZE + EDGE_SIZE*2, EDGE_SIZE)], (255,255,255), 2)
    draw.line([(EDGE_SIZE, 0), (EDGE_SIZE, IMAGE_SIZE + EDGE_SIZE*2)], (255,255,255), 2)
    draw.line([(IMAGE_SIZE + EDGE_SIZE, 0), (IMAGE_SIZE + EDGE_SIZE, IMAGE_SIZE + EDGE_SIZE*2)], (255,255,255), 2)
    draw.line([(0, IMAGE_SIZE + EDGE_SIZE), (IMAGE_SIZE + EDGE_SIZE*2, IMAGE_SIZE + EDGE_SIZE)], (255,255,255), 2)

    # Draw 0 rules
    draw.line([(EDGE_SIZE + (IMAGE_SIZE/2), 0), (EDGE_SIZE + (IMAGE_SIZE/2), EDGE_SIZE)], (255,255,255), 2)
    draw.line([0, (EDGE_SIZE + (IMAGE_SIZE/2)), (EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE/2))], (255,255,255), 2)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE/2), IMAGE_SIZE + EDGE_SIZE), (EDGE_SIZE + (IMAGE_SIZE/2), IMAGE_SIZE + EDGE_SIZE*2)], (255,255,255), 2)
    draw.line([IMAGE_SIZE + EDGE_SIZE, (EDGE_SIZE + (IMAGE_SIZE/2)), (IMAGE_SIZE + EDGE_SIZE*2, EDGE_SIZE + (IMAGE_SIZE/2))], (255,255,255), 2)

    # Draw 50 rules
    # Top
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.25), EDGE_SIZE/2), (EDGE_SIZE + (IMAGE_SIZE*0.25), EDGE_SIZE)], (255,255,255), 2)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.75), EDGE_SIZE/2), (EDGE_SIZE + (IMAGE_SIZE*0.75), EDGE_SIZE)], (255,255,255), 2)
    # Bottom
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.25), IMAGE_SIZE + EDGE_SIZE), (EDGE_SIZE + (IMAGE_SIZE*0.25), IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2)], (255,255,255), 2)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.75), IMAGE_SIZE + EDGE_SIZE), (EDGE_SIZE + (IMAGE_SIZE*0.75), IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2)], (255,255,255), 2)
    # Left
    draw.line([(EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.25)), (EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.25))], (255,255,255), 2)
    draw.line([(EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.75)), (EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.75))], (255,255,255), 2)
     # Right
    draw.line([(IMAGE_SIZE + EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.25)), (IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.25))], (255,255,255), 2)
    draw.line([(IMAGE_SIZE + EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.75)), (IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.75))], (255,255,255), 2)

# Draws a given star on the board according to the star's coordinates
def drawStar(draw, star: Star) -> None:
    # Calculate x and y pixel position on the board using the star's given x and y fields
    xPos = (star.x * 4) + (IMAGE_SIZE/2 + EDGE_SIZE)
    yPos = (star.y * 4) + (IMAGE_SIZE/2 + EDGE_SIZE)

    # Draw circle on board 
    draw.ellipse([(xPos - STAR_SIZE/2, yPos - STAR_SIZE/2),(xPos + STAR_SIZE/2, yPos + STAR_SIZE/2)], (255,255,255), (255,255,255), 0)

# Converts a string into a star object
def stringToStar(string: str) -> Star: 
    items = string.split(", ")
    starName = items[0]
    starX = float(items[1])
    starY = float(items[2])
    starZ = float(items[3])
    starColor = items[4]
    starDiameter = float(items[5])
    return Star(starX, starY, starZ, starName, starColor, starDiameter)




# Create map and draw edge rules
map = Image.new("RGB", (IMAGE_SIZE + EDGE_SIZE*2, IMAGE_SIZE + EDGE_SIZE*2), (0,0,0))
mapDraw = ImageDraw.Draw(map)
drawEdgeRule(mapDraw)

exampleStar = stringToStar("Puivert, -22, 8, -33, yellow, 10")
drawStar(mapDraw, exampleStar)

map.show()
