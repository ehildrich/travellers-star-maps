from star import *

# Function Definitions

# Converts a string into a star object
def stringToStar(string: str, sp: StarParameters) -> Star: 
    values = string.split(", ")

    # Each star needs to have 6 values
    if not (len(values) == 6):
        raise ValueError("One of the stars does not have the correct number of values, 6.")

    starName = values[0]

    try: 
        starX = float(values[1])
        starY = float(values[2])
        starZ = float(values[3])
    except: 
        raise ValueError("One of the x, y, and z values of star " + starName + " is not a valid number.")

    starColor = values[4].lower()
    # if the color isn't valid, default to white
    if (starColor not in COLORS): 
        starColor = "white"

    try: 
        starDiameter = float(values[5])
        # If the star's diameter is less than the given circle size, normalize it to the minimum circle size.
        if (starDiameter*sp.RESOLUTION < sp.CIRCLE_SIZE):
            starDiameter = sp.CIRCLE_SIZE/sp.RESOLUTION
            print("Warning: Diameter of star " + starName + " was less than the specified Circle Size parameter.")
    except: 
        raise ValueError("The circle diameter of star " + starName + " is not a valid number.")
    
    return Star(starX, starY, starZ, starName, starColor, starDiameter)

# Converts a string into a star line object
def stringToLine(string: str, sp: StarParameters) -> StarLine: 
    values = string.split(", ")

    # Each line needs to have 4 values
    if not (len(values) == 4):
        raise ValueError("One of the lines does not have the correct number of values, 4.")
    
    firstStar = values[0]
    secondStar = values[1]

    lineColor = values[2]
    # if the color isn't valid, default to white
    if (lineColor not in COLORS): 
        lineColor = "white"

    try:
        lineDiameter = float(values[3])
        # If the line's diameter is less than the given line width, normalize it to the minimum line width.
        if (lineDiameter*sp.RESOLUTION < sp.LINE_WIDTH):
            lineDiameter = sp.LINE_WIDTH/sp.RESOLUTION
            print("Warning: Line width of the line between " + firstStar + " and " + secondStar + " was less than the specified Line Width parameter.")
    except: 
        raise ValueError("The width of the line between " + firstStar + " and " + secondStar + " is not a valid number.")

    return StarLine(firstStar, secondStar, lineColor, lineDiameter)

# Opens a text file and returns a list of the file's text lines, stripped of whitespace
def getFileStrings(filename: str) -> list:
    # Open map text file
    try:
        textFile = open(filename, "r")
    except: 
        raise FileNotFoundError("The text file does not exist.")
    else: 
        with textFile as stars:
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
def getStarInfo(filename: str, orientation: tuple) -> StarInfo:
    items = getFileStrings(filename)
    
    # Get the separator between the stars and lines in the text lines
    # If a separator is missing, raise an error. 
    try: 
        starIndex = items.index("STAR")
        connectIndex = items.index("CONNECT")

        # This index is not used, this is purely to ensure proper formatting of the text file
        paramIndex = items.index("PARAMETER")
    except:
        raise ValueError("A section header is missing.")

    # Take only the parameters and convert into a dictionary
    paramStrings = items[1:starIndex]
    if not (len(paramStrings) == 6):
        raise ValueError("The number of parameters given is incorrect. There must be 6 parameters: Image Size, Edge Size, Line Width, Star Size, Circle Size, and Font Size.")

    params = {}
    try: 
        for paramString in paramStrings:
            param = paramString.split(": ")
            params[param[0]] = float(param[1])
    except:
        raise ValueError("There was an error with the format of one of the parameters. All of the values must be numbers.")
    # Create the StarParameters object to use with the rest of the items
    starParameters =StarParameters(params['Image Size'], 
                                    params['Edge Size'], 
                                    params['Line Width'], 
                                    params['Star Size'], 
                                    params['Circle Size'], 
                                    params['Font Size'], 
                                    orientation)

    # Take only the star items and convert into a list of star objects
    starStrings = items[(starIndex + 1):connectIndex]
    stars = []
    for starString in starStrings:
        stars.append(stringToStar(starString, starParameters))

    # Take only the line items and convert into a list of line objects
    lineStrings = items[(connectIndex + 1):]
    lines = []
    for lineString in lineStrings:
        lines.append(stringToLine(lineString, starParameters))

    # Return a StarInfo containing both lists and the paramter object
    return StarInfo(stars, lines, starParameters)