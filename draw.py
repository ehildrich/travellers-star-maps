from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
import math

from star import *
sp = StarParameters()

# Function Definitions

# Draws the gridlines at the edges of the board and the centerlines that pass through the middle of board
def drawEdgeRule(draw: ImageDraw) -> None: 
    # Start with center lines
    draw.line([(0, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2)), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2))], sp.COLORS["gray"], 1)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), 0), (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], sp.COLORS["gray"], 1)

    #Draw map edges
    draw.line([(0, sp.EDGE_SIZE), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.EDGE_SIZE)], sp.COLORS["white"], 2)
    draw.line([(sp.EDGE_SIZE, 0), (sp.EDGE_SIZE, sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], sp.COLORS["white"], 2)
    draw.line([(sp.IMAGE_SIZE + sp.EDGE_SIZE, 0), (sp.IMAGE_SIZE + sp.EDGE_SIZE, sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], sp.COLORS["white"], 2)
    draw.line([(0, sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.IMAGE_SIZE + sp.EDGE_SIZE)], sp.COLORS["white"], 2)

    # Draw 0 rules
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), 0), (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.EDGE_SIZE)], sp.COLORS["white"], 2)
    draw.line([0, (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2)), (sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2))], sp.COLORS["white"], 2)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], sp.COLORS["white"], 2)
    draw.line([sp.IMAGE_SIZE + sp.EDGE_SIZE, (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2)), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2))], sp.COLORS["white"], 2)

    # Draw 50 rules
    # Top
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.EDGE_SIZE/2), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.EDGE_SIZE)], sp.COLORS["white"], 2)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.EDGE_SIZE/2), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.EDGE_SIZE)], sp.COLORS["white"], 2)
    # Bottom
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2)], sp.COLORS["white"], 2)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2)], sp.COLORS["white"], 2)
    # Left
    draw.line([(sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25)), (sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25))], sp.COLORS["white"], 2)
    draw.line([(sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75)), (sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75))], sp.COLORS["white"], 2)
     # Right
    draw.line([(sp.IMAGE_SIZE + sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25)), (sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25))], sp.COLORS["white"], 2)
    draw.line([(sp.IMAGE_SIZE + sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75)), (sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75))], sp.COLORS["white"], 2)

# Returns either the x, y, or z position of a star on the board
def getPos(star: Star, type: str) -> float: 
    if (type.lower() == "x"):
        return (sp.IMAGE_SIZE/2 + sp.EDGE_SIZE) + (star.x * sp.RESOLUTION)
    if (type.lower() == "y"):
        return (sp.IMAGE_SIZE/2 + sp.EDGE_SIZE) - (star.y * sp.RESOLUTION)
    if (type.lower() == "z"):
        return (sp.IMAGE_SIZE/2 + sp.EDGE_SIZE) + (star.z * sp.RESOLUTION)
    else: 
        return -1

# Given a string of text, returns how many pixels wide that text is when drawn on the board
def getTextWidth(font: ImageFont.FreeTypeFont, string: str) -> int:
    testImage = Image.new("RGB", (75,75))
    testDraw = ImageDraw.Draw(testImage)

    testDraw.text((0,0), string, sp.COLORS["white"], font)
    bound = testImage.getbbox()

    return bound[2] - bound[0]

# Draws a given star on the board according to the star's coordinates
def drawStar(draw: ImageDraw, font: ImageFont.FreeTypeFont, star: Star) -> None:
    # Calculate x and y pixel position on the board using the star's given x and y fields
    xPos = getPos(star, "x")
    yPos = getPos(star, "y")

    starSize = ((star.z + 100) / 200) * sp.MAX_STAR_SIZE

    # Draw circle on board 
    draw.ellipse([(xPos - starSize/2, yPos - starSize/2),(xPos + starSize/2, yPos + starSize/2)], fill=sp.COLORS["white"])

    # Draw outside circle
    draw.ellipse([(xPos - sp.CIRCLE_SIZE/2, yPos - sp.CIRCLE_SIZE/2),(xPos + sp.CIRCLE_SIZE/2, yPos + sp.CIRCLE_SIZE/2)], outline=sp.COLORS[star.color], width=sp.LINE_WIDTH)

    # Add name and Z-axis below. Text is placed so that it appears just to the right of the star's circle. 
    # Check if any of the text will go past the rightmost edge rule. If so move it to the right of the star
    if (xPos + sp.CIRCLE_SIZE + max(getTextWidth(font, star.name), getTextWidth(font, str(star.z))) > sp.IMAGE_SIZE + sp.EDGE_SIZE):
        draw.text((xPos - sp.CIRCLE_SIZE - getTextWidth(font, star.name), yPos - sp.FONT_SIZE), star.name, sp.COLORS["white"], font)
        draw.text((xPos - sp.CIRCLE_SIZE - getTextWidth(font, str(star.z)), yPos), str(star.z), sp.COLORS["white"], font)
    else:
        # Otherwise draw the text to the right of the star
        draw.text((xPos + sp.CIRCLE_SIZE, yPos - sp.FONT_SIZE), str(star.name), sp.COLORS["white"], font)
        draw.text((xPos + sp.CIRCLE_SIZE, yPos), str(star.z), sp.COLORS["white"], font)

# Draws a line between two stars on the board
def drawLine(draw: ImageDraw, line: StarLine, info: StarInfo) -> None: 
    # Get both stars
    firstStar = None
    secondStar = None
    for star in info.stars:
        if (star.name == line.firstStar): 
            firstStar = star
        if (star.name == line.secondStar): 
            secondStar = star
    
    # TODO handle if stars are not found - issue a warning?
    if (firstStar != None) and (secondStar != None): 
        # Get the positions of the stars on the board
        firstStarX = getPos(firstStar, "x")
        firstStarY =  getPos(firstStar, "y")
        secondStarX = getPos(secondStar, "x")
        secondStarY = getPos(secondStar, "y")

        # Get the distance between the two stars
        distance = math.sqrt((secondStarX - firstStarX)**2 + (secondStarY - firstStarY)**2)

        # Get the ratio between the distance and the offset
        distanceRatio = sp.LINE_OFFSET / distance
        # Use the ratio to calculate the points on the line that are a offset's length away from the stars
        firstOffset = ((1 - distanceRatio) * firstStarX + distanceRatio * secondStarX, (1 - distanceRatio) * firstStarY + distanceRatio * secondStarY) 
        secondOffset = ((1 - distanceRatio) * secondStarX + distanceRatio * firstStarX, (1 - distanceRatio) * secondStarY + distanceRatio * firstStarY) 

        # Draw the line with the offset coordinates
        draw.line([firstOffset, secondOffset], sp.COLORS[line.color], sp.LINE_WIDTH)

# Grabs a basic sans-serif font of the given size
# TODO throw error if no font found
def getFont(size: int) -> ImageFont.FreeTypeFont:
    sansSerif = font_manager.FontProperties(family = "monospace", style="normal")
    filePath = font_manager.findfont(sansSerif)

    font = ImageFont.truetype(filePath, size)
    return font

def drawBoard(draw: ImageDraw, starmapInfo: StarInfo) -> None: 
    # First draw map edges
    drawEdgeRule(draw)

    typeFont = getFont(sp.FONT_SIZE)

    # Draw lines before stars so the stars appear on top
    for line in starmapInfo.lines: 
        drawLine(draw, line, starmapInfo)

    # Draw stars
    for star in starmapInfo.stars:
        drawStar(draw, typeFont, star)

def createBoard(info: StarInfo) -> Image:
    # Create map, draw object, and get the text font
    map = Image.new("RGB", (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.IMAGE_SIZE + sp.EDGE_SIZE*2), (0,0,0))
    mapDraw = ImageDraw.Draw(map)

    drawBoard(mapDraw, info)

    return map