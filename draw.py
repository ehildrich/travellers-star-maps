from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
from datetime import datetime
import os
import math

from star import *

# Function Definitions

# Draws the gridlines at the edges of the board and the centerlines that pass through the middle of board
def drawEdgeRule(sp: StarParameters, font: ImageFont.FreeTypeFont, draw: ImageDraw) -> None: 
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

    # Draw axis labels
    draw.text((sp.IMAGE_SIZE + sp.EDGE_SIZE - getTextWidth(font, sp.orientation[0]) - sp.LINE_WIDTH, sp.IMAGE_SIZE + sp.EDGE_SIZE + sp.LINE_WIDTH), sp.orientation[0], COLORS["white"], font)
    draw.text((sp.EDGE_SIZE - getTextWidth(font, sp.orientation[1]) - sp.LINE_WIDTH, sp.EDGE_SIZE + sp.LINE_WIDTH), sp.orientation[1], COLORS["white"], font)


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

def getDistanceRatio(star: Star, sp: StarParameters, distance: float): 
    # Calculate offset based on the star's circle diameter
    return ((star.diameter*sp.RESOLUTION)/2) / distance

# Draws a given star on the board according to the star's coordinates
def drawStar(sp: StarParameters, draw: ImageDraw, font: ImageFont.FreeTypeFont, star: Star) -> None:
    # Calculate bottom and side pixel position on the board using the star's given fields
    bottomPos = getPos(sp, star, sp.orientation[0])
    sidePos = getPos(sp, star, sp.orientation[1])

    # Get the depth positin of the star
    if (sp.orientation[2] == "x"):
        depthPos = star.x
    elif (sp.orientation[2] == "y"):
        depthPos = star.y
    else:
        depthPos = star.z
    # Calculate star size. It must be at least 1
    starSize = (((depthPos + 100) / 200) * sp.MAX_STAR_SIZE) if (((depthPos + 100) / 200) * sp.MAX_STAR_SIZE) > 0 else 1

    # Draw circle on board 
    draw.ellipse([(bottomPos - starSize/2, sidePos - starSize/2),(bottomPos + starSize/2, sidePos + starSize/2)], fill=COLORS["white"])

    # Draw outside circle
    circleSize = star.diameter*sp.RESOLUTION
    draw.ellipse([(bottomPos - circleSize/2, sidePos - circleSize/2),(bottomPos + circleSize/2, sidePos + circleSize/2)], outline=COLORS[star.color], width=sp.LINE_WIDTH)

    # Add name and Z-axis below. Text is placed so that it appears just to the right of the star's circle. 
    # Check if any of the text will go past the rightmost edge rule. If so move it to the right of the star
    if (bottomPos + circleSize + max(getTextWidth(font, star.name), getTextWidth(font, str(depthPos))) > sp.IMAGE_SIZE + sp.EDGE_SIZE):
        draw.text((bottomPos - circleSize/2 - getTextWidth(font, star.name) - sp.LINE_WIDTH - 4, sidePos - sp.FONT_SIZE), star.name, COLORS["white"], font)
        draw.text((bottomPos - circleSize/2 - getTextWidth(font, str(depthPos)) - sp.LINE_WIDTH - 4, sidePos), str(depthPos), COLORS["white"], font)
    else:
        # Otherwise draw the text to the right of the star
        draw.text((bottomPos + circleSize/2 + sp.LINE_WIDTH + 4, sidePos - sp.FONT_SIZE), str(star.name), COLORS["white"], font)
        draw.text((bottomPos + circleSize/2 + sp.LINE_WIDTH + 4, sidePos), str(star.z), COLORS["white"], font)

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
        firstStarBottom = getPos(sp, firstStar, sp.orientation[0])
        firstStarSide =  getPos(sp, firstStar, sp.orientation[1])
        secondStarBottom = getPos(sp, secondStar, sp.orientation[0])
        secondStarSide = getPos(sp, secondStar, sp.orientation[1])

        # Get the distance between the two stars
        distance = math.sqrt((secondStarBottom - firstStarBottom)**2 + (secondStarSide - firstStarSide)**2)

        firstDistanceRatio = getDistanceRatio(firstStar, sp, distance)
        secondDistanceRatio = getDistanceRatio(secondStar, sp, distance)
        
        # Use the ratio to calculate the points on the line that are an offset's length away from the stars on each end
        firstOffset = ((1 - firstDistanceRatio) * firstStarBottom + firstDistanceRatio * secondStarBottom, (1 - firstDistanceRatio) * firstStarSide + firstDistanceRatio * secondStarSide) 
        secondOffset = ((1 - secondDistanceRatio) * secondStarBottom + secondDistanceRatio * firstStarBottom, (1 - secondDistanceRatio) * secondStarSide + secondDistanceRatio * firstStarSide) 

        # Draw the line with the offset coordinates
        draw.line([firstOffset, secondOffset], COLORS[line.color], int(line.diameter*4))
    else: 
        raise AttributeError("One or more stars " + line.firstStar + " and " + line.secondStar + " specified in a line was not found.")

# Grabs a basic monospace font of the given size
def getFont(size: int) -> ImageFont.FreeTypeFont:
    sansSerif = font_manager.FontProperties(family = "monospace", style="normal")
    filePath = font_manager.findfont(sansSerif)

    font = ImageFont.truetype(filePath, size)
    return font

# Draws all elements of the board
def drawBoard(draw: ImageDraw, starmapInfo: StarInfo) -> None: 
    # Grab the font to use on the stars
    typeFont = getFont(starmapInfo.params.FONT_SIZE)

    # First draw map edges
    drawEdgeRule(starmapInfo.params, typeFont, draw)

    # Draw lines before stars so the stars and circles appear on top
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
    fileName = OUTPUT + dateString + ".png"
    image.save(fileName)
    print("Image saved.")

    # Finish off by opening the completed image for the user to see
    try: 
        finishedImage = Image.open(fileName)
    except: 
        raise FileNotFoundError("There was a problem opening the generated image.")
    else:
        finishedImage.show()