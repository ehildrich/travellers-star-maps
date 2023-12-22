from star import *

# Function Definitions

# Converts a string into a star object
def stringToStar(string: str) -> Star: 
    values = string.split(", ")

    # Each star needs to have 6 values
    if not (len(values) == 6):
        raise ValueError("Stars must have 6 values each.")

    starName = values[0]
    starX = float(values[1])
    starY = float(values[2])
    starZ = float(values[3])
    starColor = values[4]

    # if the color isn't valid, default to white
    if (starColor not in COLORS): 
        starColor = "white"

    starDiameter = float(values[5])
    return Star(starX, starY, starZ, starName, starColor, starDiameter)

# Converts a string into a star line object
def stringToLine(string: str) -> StarLine: 
    values = string.split(", ")

    # Each line needs to have 4 values
    if not (len(values) == 4):
        raise ValueError("Lines must have 4 values each.")
    
    firstStar = values[0]
    secondStar = values[1]
    lineColor = values[2]
    lineDiameter = float(values[3])
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
def getStarInfo(filename: str) -> StarInfo:
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
    params = {}
    for paramString in paramStrings:
        param = paramString.split(": ")
        params[param[0]] = int(param[1])

    # Take only the star items and convert into a list of star objects
    starStrings = items[(starIndex + 1):connectIndex]
    stars = []
    for starString in starStrings:
        # If there was an error, raise it to the next level
        try: 
            stars.append(stringToStar(starString))
        except:
            raise

    # Take only the line items and convert into a list of line objects
    lineStrings = items[(connectIndex + 1):]
    lines = []
    for lineString in lineStrings:
        # If there was an error, raise it to the next level
        try:
            lines.append(stringToLine(lineString))
        except:
            raise

    # Return a StarInfo containing both lists and a paramter object made out of the dictionary
    return StarInfo(stars, lines, StarParameters(params['Image Size'], 
                                                 params['Edge Size'], 
                                                 params['Line Width'], 
                                                 params['Line Offset'], 
                                                 params['Star Size'], 
                                                 params['Circle Size'], 
                                                 params['Font Size']))