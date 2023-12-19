from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
import math

from star import *
from reader import getStarInfo



# Global Variables

IMAGE_SIZE = 800
RESOLUTION = IMAGE_SIZE/200
EDGE_SIZE = 20
LINE_WIDTH = 1
LINE_OFFSET = 10
STAR_SIZE = 8
FONT_SIZE = 12
COLORS = {
    "blue" : (0, 25, 245), 
    "brown" : (123, 68, 0), 
    "gray" : (50, 50, 50), 
    "green" : (25, 224, 25), 
    "orange" : (255, 121, 0), 
    "purple" : (106, 1, 250), 
    "red" : (214, 16, 16), 
    "white" : (255,255,255), 
    "yellow" : (249, 218, 2) 
}



# Function Definitions

# Draws the gridlines at the edges of the board and the centerlines that pass through the middle of board
def drawEdgeRule(draw): 
    # Start with center lines
    draw.line([(0, EDGE_SIZE + (IMAGE_SIZE/2)), (IMAGE_SIZE + EDGE_SIZE*2, EDGE_SIZE + (IMAGE_SIZE/2))],  COLORS["gray"], 1)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE/2), 0), (EDGE_SIZE + (IMAGE_SIZE/2), IMAGE_SIZE + EDGE_SIZE*2)],  COLORS["gray"], 1)

    #Draw map edges
    draw.line([(0, EDGE_SIZE), (IMAGE_SIZE + EDGE_SIZE*2, EDGE_SIZE)], COLORS["white"], 2)
    draw.line([(EDGE_SIZE, 0), (EDGE_SIZE, IMAGE_SIZE + EDGE_SIZE*2)], COLORS["white"], 2)
    draw.line([(IMAGE_SIZE + EDGE_SIZE, 0), (IMAGE_SIZE + EDGE_SIZE, IMAGE_SIZE + EDGE_SIZE*2)], COLORS["white"], 2)
    draw.line([(0, IMAGE_SIZE + EDGE_SIZE), (IMAGE_SIZE + EDGE_SIZE*2, IMAGE_SIZE + EDGE_SIZE)], COLORS["white"], 2)

    # Draw 0 rules
    draw.line([(EDGE_SIZE + (IMAGE_SIZE/2), 0), (EDGE_SIZE + (IMAGE_SIZE/2), EDGE_SIZE)], COLORS["white"], 2)
    draw.line([0, (EDGE_SIZE + (IMAGE_SIZE/2)), (EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE/2))], COLORS["white"], 2)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE/2), IMAGE_SIZE + EDGE_SIZE), (EDGE_SIZE + (IMAGE_SIZE/2), IMAGE_SIZE + EDGE_SIZE*2)], COLORS["white"], 2)
    draw.line([IMAGE_SIZE + EDGE_SIZE, (EDGE_SIZE + (IMAGE_SIZE/2)), (IMAGE_SIZE + EDGE_SIZE*2, EDGE_SIZE + (IMAGE_SIZE/2))], COLORS["white"], 2)

    # Draw 50 rules
    # Top
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.25), EDGE_SIZE/2), (EDGE_SIZE + (IMAGE_SIZE*0.25), EDGE_SIZE)], COLORS["white"], 2)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.75), EDGE_SIZE/2), (EDGE_SIZE + (IMAGE_SIZE*0.75), EDGE_SIZE)], COLORS["white"], 2)
    # Bottom
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.25), IMAGE_SIZE + EDGE_SIZE), (EDGE_SIZE + (IMAGE_SIZE*0.25), IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2)], COLORS["white"], 2)
    draw.line([(EDGE_SIZE + (IMAGE_SIZE*0.75), IMAGE_SIZE + EDGE_SIZE), (EDGE_SIZE + (IMAGE_SIZE*0.75), IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2)], COLORS["white"], 2)
    # Left
    draw.line([(EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.25)), (EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.25))], COLORS["white"], 2)
    draw.line([(EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.75)), (EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.75))], COLORS["white"], 2)
     # Right
    draw.line([(IMAGE_SIZE + EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.25)), (IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.25))], COLORS["white"], 2)
    draw.line([(IMAGE_SIZE + EDGE_SIZE, EDGE_SIZE + (IMAGE_SIZE*0.75)), (IMAGE_SIZE + EDGE_SIZE + EDGE_SIZE/2, EDGE_SIZE + (IMAGE_SIZE*0.75))], COLORS["white"], 2)

# Returns either the x, y, or z position of a star on the board
def getPos(star: Star, type: str) -> float: 
    if (type.lower() == "x"):
        return (star.x * RESOLUTION) + (IMAGE_SIZE/2 + EDGE_SIZE)
    if (type.lower() == "y"):
        return (star.y * RESOLUTION) + (IMAGE_SIZE/2 + EDGE_SIZE)
    if (type.lower() == "z"):
        return (star.z * RESOLUTION) + (IMAGE_SIZE/2 + EDGE_SIZE)
    else: 
        return -1

# Draws a given star on the board according to the star's coordinates
def drawStar(draw, font, star: Star) -> None:
    # Calculate x and y pixel position on the board using the star's given x and y fields
    xPos = getPos(star, "x")
    yPos = getPos(star, "y")

    # Draw circle on board 
    draw.ellipse([(xPos - STAR_SIZE/2, yPos - STAR_SIZE/2),(xPos + STAR_SIZE/2, yPos + STAR_SIZE/2)], COLORS["white"], COLORS["white"], 0)

    # Add z-axis below
    draw.text((xPos - STAR_SIZE*2, yPos + STAR_SIZE*1.5), str(star.z), COLORS["white"], font)

# Draws a line between two stars on the board
def drawLine(draw, line: StarLine, info: StarInfo) -> None: 
    # Get both stars
    firstStar = None
    secondStar = None
    for star in info.stars:
        if (star.name == line.firstStar): 
            firstStar = star
        if (star.name == line.secondStar): 
            secondStar = star
    
    if (firstStar != None) and (secondStar != None): 
        # Get the positions of the stars on the board
        firstStarX = getPos(firstStar, "x")
        firstStarY =  getPos(firstStar, "y")
        secondStarX = getPos(secondStar, "x")
        secondStarY = getPos(secondStar, "y")

        # Get the distance between the two stars
        distance = math.sqrt((secondStarX - firstStarX)**2 + (secondStarY - firstStarY)**2)

        # Get the ratio between the distance and the offset
        distanceRatio = LINE_OFFSET / distance
        # Use the ratio to calculate the points on the line that are a offset's length away from the stars
        firstOffset = ((1 - distanceRatio) * firstStarX + distanceRatio * secondStarX, (1 - distanceRatio) * firstStarY + distanceRatio * secondStarY) 
        secondOffset = ((1 - distanceRatio) * secondStarX + distanceRatio * firstStarX, (1 - distanceRatio) * secondStarY + distanceRatio * firstStarY) 

        # Draw the line with the offset coordinates
        draw.line([firstOffset, secondOffset], COLORS[line.color], LINE_WIDTH)

def drawBoard(draw, font, starmapInfo: StarInfo) -> None: 
    # First draw map edges
    drawEdgeRule(draw)

    # Draw lines before stars so the stars appear on top
    for line in starmapInfo.lines: 
        drawLine(draw, line, starmapInfo)

    # Draw stars
    for star in starmapInfo.stars:
        drawStar(draw, font, star)

# Grabs a basic sans-serif font of the given size
# TODO throw error if no font found
def getFont(size: int) -> ImageFont.FreeTypeFont:
    sansSerif = font_manager.FontProperties(family = "sans-serif", style="normal")
    filePath = font_manager.findfont(sansSerif)

    font = ImageFont.truetype(filePath, size)
    return font





# MAIN
# Create map, draw object, and get the text font
map = Image.new("RGB", (IMAGE_SIZE + EDGE_SIZE*2, IMAGE_SIZE + EDGE_SIZE*2), (0,0,0))
mapDraw = ImageDraw.Draw(map)
typeFont = getFont(FONT_SIZE)

# Get starmap information
starmapInfo = getStarInfo()

# Draw board items
drawBoard(mapDraw, typeFont, starmapInfo)

# Show the map
map.show()
