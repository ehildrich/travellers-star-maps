from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager

from star import Star
from reader import getStarInfo



# Global Variables
IMAGE_SIZE = 800
EDGE_SIZE = 20
STAR_SIZE = 8
FONT_SIZE = 12



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
def drawStar(draw, font, star: Star) -> None:
    # Calculate x and y pixel position on the board using the star's given x and y fields
    xPos = (star.x * 4) + (IMAGE_SIZE/2 + EDGE_SIZE)
    yPos = (star.y * 4) + (IMAGE_SIZE/2 + EDGE_SIZE)

    # Draw circle on board 
    draw.ellipse([(xPos - STAR_SIZE/2, yPos - STAR_SIZE/2),(xPos + STAR_SIZE/2, yPos + STAR_SIZE/2)], (255,255,255), (255,255,255), 0)

    # Add z-axis below
    draw.text((xPos - STAR_SIZE*2, yPos + STAR_SIZE*1.5), str(star.z), (255,255,255), font)

# Grabs a basic sans-serif font of the given size
# TODO throw error if no font found
def getFont(size: int) -> ImageFont.FreeTypeFont:
    sansSerif = font_manager.FontProperties(family = "sans-serif", style="normal")
    filePath = font_manager.findfont(sansSerif)

    font = ImageFont.truetype(filePath, size)
    return font



# Create map, draw object, and get the text font
map = Image.new("RGB", (IMAGE_SIZE + EDGE_SIZE*2, IMAGE_SIZE + EDGE_SIZE*2), (0,0,0))
mapDraw = ImageDraw.Draw(map)
typeFont = getFont(FONT_SIZE)

# Draw map edges
drawEdgeRule(mapDraw)

# Get starmap information
starmapInfo = getStarInfo()
# Draw stars
for star in starmapInfo.stars:
    drawStar(mapDraw, typeFont, star)

map.show()
