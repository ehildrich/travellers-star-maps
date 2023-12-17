import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

# Global Variables
IMAGE_SIZE = 800
EDGE_SIZE = 20

# Class Definitions
class Star: 
    def __init__(self, x, y, z, name):
        pass

# Function Definitions
def drawEdgeRule(draw): 
    # Start with center lines
    draw.line([(0, EDGE_SIZE + (IMAGE_SIZE/2)), (IMAGE_SIZE + EDGE_SIZE*2, EDGE_SIZE + (IMAGE_SIZE/2))], (50,50,50), 2)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE/2), 0), (EDGE_SIZE + (IMAGE_SIZE/2), IMAGE_SIZE + EDGE_SIZE*2)], (50,50,50), 2)

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




# Create map and draw edge rules
map = Image.new("RGB", (IMAGE_SIZE + EDGE_SIZE*2, IMAGE_SIZE + EDGE_SIZE*2), (0,0,0))
mapDraw = ImageDraw.Draw(map)
drawEdgeRule(mapDraw)

map.show()



