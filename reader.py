from star import *
sp = StarParameters()

# Function Definitions

# Converts a string into a star object
def stringToStar(string: str) -> Star: 
    values = string.split(", ")
    starName = values[0]
    starX = float(values[1])
    starY = float(values[2])
    starZ = float(values[3])
    starColor = values[4]

    # if the color isn't valid, default to white
    if (starColor not in sp.COLORS): 
        starColor = "white"

    starDiameter = float(values[5])
    return Star(starX, starY, starZ, starName, starColor, starDiameter)

# Converts a string into a star line object
def stringToLine(string: str) -> StarLine: 
    values = string.split(", ")
    firstStar = values[0]
    secondStar = values[1]
    lineColor = values[2]
    lineDiameter = float(values[3])
    return StarLine(firstStar, secondStar, lineColor, lineDiameter)

# Opens a text file and returns a list of the file's text lines, stripped of whitespace
# TODO throw error if file not found
def getFileStrings():
    # Open map text file
    with open("map.txt", "r") as stars:
        # Read all lines and strip whitespace from each
        lines = stars.readlines()
        items = []
        for line in lines:
            strippedLine = line.rstrip().lstrip()

            # Ignore blank lines
            if(strippedLine == ""): 
                continue
            else: 
                items.append(strippedLine)
    return items

# Given a list of strings from a properly formatted starmap text file, returns
# a StarInfo object containing a list of stars and a list of lines
# TODO throw error if section headers do not exist
def getStarInfo():
    items = getFileStrings()
    
    # Get the separator between the stars and lines in the text lines
    connectIndex = items.index("CONNECT")

    # Take only the star items and convert into a list of star objects
    starStrings = items[1:connectIndex]
    stars = []
    for starString in starStrings:
        stars.append(stringToStar(starString))

    # Take only the line items and convert into a list of line objects
    lineStrings = items[(connectIndex + 1):]
    lines = []
    for lineString in lineStrings:
        lines.append(stringToLine(lineString))

    # Return a StarInfo containing both lists
    return StarInfo(stars, lines)