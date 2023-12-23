from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
from datetime import datetime
import os
import math

from star import *

# Function Definitions

# Draws the gridlines at the edges of the board and the centerlines that pass through the middle of board
def drawEdgeRule(sp: StarParameters, draw: ImageDraw) -> None: 
    # Start with center lines
    draw.line([(0, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2)), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2))], COLORS["gray"], 1)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), 0), (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], COLORS["gray"], 1)

    #Draw map edges
    draw.line([(0, sp.EDGE_SIZE), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.EDGE_SIZE)], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(sp.EDGE_SIZE, 0), (sp.EDGE_SIZE, sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(sp.IMAGE_SIZE + sp.EDGE_SIZE, 0), (sp.IMAGE_SIZE + sp.EDGE_SIZE, sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(0, sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.IMAGE_SIZE + sp.EDGE_SIZE)], COLORS["white"], sp.LINE_WIDTH)

    # Draw 0 rules
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), 0), (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.EDGE_SIZE)], COLORS["white"], sp.LINE_WIDTH)
    draw.line([0, (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2)), (sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2))], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2), sp.IMAGE_SIZE + sp.EDGE_SIZE*2)], COLORS["white"], sp.LINE_WIDTH)
    draw.line([sp.IMAGE_SIZE + sp.EDGE_SIZE, (sp.EDGE_SIZE + (sp.IMAGE_SIZE/2)), (sp.IMAGE_SIZE + sp.EDGE_SIZE*2, sp.EDGE_SIZE + (sp.IMAGE_SIZE/2))], COLORS["white"], sp.LINE_WIDTH)

    # Draw 50 rules
    # Top
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.EDGE_SIZE/2), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.EDGE_SIZE)], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.EDGE_SIZE/2), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.EDGE_SIZE)], COLORS["white"], sp.LINE_WIDTH)
    # Bottom
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25), sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2)], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.IMAGE_SIZE + sp.EDGE_SIZE), (sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75), sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2)], COLORS["white"], sp.LINE_WIDTH)
    # Left
    draw.line([(sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25)), (sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25))], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75)), (sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75))], COLORS["white"], sp.LINE_WIDTH)
     # Right
    draw.line([(sp.IMAGE_SIZE + sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25)), (sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.25))], COLORS["white"], sp.LINE_WIDTH)
    draw.line([(sp.IMAGE_SIZE + sp.EDGE_SIZE, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75)), (sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.EDGE_SIZE/2, sp.EDGE_SIZE + (sp.IMAGE_SIZE*0.75))], COLORS["white"], sp.LINE_WIDTH)

# Returns either the x, y, or z position of a star on the board
def getPos(sp: StarParameters, star: Star, type: str) -> float: 
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
    testImage = Image.new("RGB", ((len(string)*font.size)*2,100))
    testDraw = ImageDraw.Draw(testImage)

    testDraw.text((0,0), string, COLORS["white"], font)
    bound = testImage.getbbox()
    
    return bound[2] - bound[0]

# Draws a given star on the board according to the star's coordinates
def drawStar(sp: StarParameters, draw: ImageDraw, font: ImageFont.FreeTypeFont, star: Star) -> None:
    # Calculate x and y pixel position on the board using the star's given x and y fields
    xPos = getPos(sp, star, "x")
    yPos = getPos(sp, star, "y")

    starSize = ((star.z + 100) / 200) * sp.MAX_STAR_SIZE

    # Draw circle on board 
    draw.ellipse([(xPos - starSize/2, yPos - starSize/2),(xPos + starSize/2, yPos + starSize/2)], fill=COLORS["white"])

    # Draw outside circle
    if (star.diameter*4 < sp.CIRCLE_SIZE): 
        circleSize = sp.CIRCLE_SIZE
        print("Warning: Diameter of star " + star.name + " was less than the specified Circle Size parameter.")
    else:
        circleSize = star.diameter*4
    
    draw.ellipse([(xPos - circleSize/2, yPos - circleSize/2),(xPos + circleSize/2, yPos + circleSize/2)], outline=COLORS[star.color], width=sp.LINE_WIDTH)

    # Add name and Z-axis below. Text is placed so that it appears just to the right of the star's circle. 
    # Check if any of the text will go past the rightmost edge rule. If so move it to the right of the star
    if (xPos + circleSize + max(getTextWidth(font, star.name), getTextWidth(font, str(star.z))) > sp.IMAGE_SIZE + sp.EDGE_SIZE):
        draw.text((xPos - circleSize/2 - getTextWidth(font, star.name) - sp.LINE_WIDTH - 4, yPos - sp.FONT_SIZE), star.name, COLORS["white"], font)
        draw.text((xPos - circleSize/2 - getTextWidth(font, str(star.z)) - sp.LINE_WIDTH - 4, yPos), str(star.z), COLORS["white"], font)
    else:
        # Otherwise draw the text to the right of the star
        draw.text((xPos + circleSize/2 + sp.LINE_WIDTH + 4, yPos - sp.FONT_SIZE), str(star.name), COLORS["white"], font)
        draw.text((xPos + circleSize/2 + sp.LINE_WIDTH + 4, yPos), str(star.z), COLORS["white"], font)

# Draws a line between two stars on the board
def drawLine(sp: StarParameters, draw: ImageDraw, line: StarLine, info: StarInfo) -> None: 
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
        firstStarX = getPos(sp, firstStar, "x")
        firstStarY =  getPos(sp, firstStar, "y")
        secondStarX = getPos(sp, secondStar, "x")
        secondStarY = getPos(sp, secondStar, "y")

        # Get the distance between the two stars
        distance = math.sqrt((secondStarX - firstStarX)**2 + (secondStarY - firstStarY)**2)

        # If the line offset is less than the star's circle size, make it larger to compensate
        if (star.diameter*4 > sp.CIRCLE_SIZE): 
            offset = (star.diameter*4)/2
        else:
            offset = sp.LINE_OFFSET
        
        # Get the ratio between the distance and the offset
        distanceRatio = offset / distance
        # Use the ratio to calculate the points on the line that are a offset's length away from the stars
        firstOffset = ((1 - distanceRatio) * firstStarX + distanceRatio * secondStarX, (1 - distanceRatio) * firstStarY + distanceRatio * secondStarY) 
        secondOffset = ((1 - distanceRatio) * secondStarX + distanceRatio * firstStarX, (1 - distanceRatio) * secondStarY + distanceRatio * firstStarY) 

        # Draw the line with the offset coordinates
        draw.line([firstOffset, secondOffset], COLORS[line.color], sp.LINE_WIDTH)
    else: 
        raise AttributeError("One or more stars " + line.firstStar + " and " + line.secondStar + " specified in a line was not found.")

# Grabs a basic sans-serif font of the given size
def getFont(size: int) -> ImageFont.FreeTypeFont:
    sansSerif = font_manager.FontProperties(family = "monospace", style="normal")
    filePath = font_manager.findfont(sansSerif)

    font = ImageFont.truetype(filePath, size)
    return font

# Draws all elements of the board
def drawBoard(draw: ImageDraw, starmapInfo: StarInfo) -> None: 
    # First draw map edges
    drawEdgeRule(starmapInfo.params, draw)

    typeFont = getFont(starmapInfo.params.FONT_SIZE)

    # Draw lines before stars so the stars appear on top
    for line in starmapInfo.lines: 
        drawLine(starmapInfo.params, draw, line, starmapInfo)

    # Draw stars
    for star in starmapInfo.stars:
        drawStar(starmapInfo.params, draw, typeFont, star)

# Creates the board image and then draws board elements onto it. Returns the completed image
def createBoard(info: StarInfo) -> Image:
    # Create map, draw object, and get the text font
    map = Image.new("RGB", (info.params.IMAGE_SIZE + info.params.EDGE_SIZE*2, info.params.IMAGE_SIZE + info.params.EDGE_SIZE*2), (0,0,0))
    mapDraw = ImageDraw.Draw(map)

    drawBoard(mapDraw, info)

    return map

# Saves a given image to the output directory as a PNG
def saveImage(image: Image) -> None:
    # If an output directory doesn't already exist, create it
    OUTPUT = "./output/"
    if not (os.path.exists(OUTPUT)):
        os.mkdir(OUTPUT)

    # The filename is the current time up to the microsecond
    dateString = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")

    # Save the image in the output directory
    image.save(OUTPUT + dateString + ".png")