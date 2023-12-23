from reader import getStarInfo
from draw import createBoard, saveImage
import sys

def findUnusedThird(arg1, arg2, validValues: list) -> int:
    # Find the indexes of the two arguments in the valid values list
    arg1Index = validValues.index(arg1)
    arg2Index = validValues.index(arg2)

    # Check each set of indexes to find what the third value's index must be
    if ((arg1Index == 0) and (arg2Index == 1)) or ((arg1Index == 1) and (arg2Index == 0)):
        return 2
    elif ((arg1Index == 1) and (arg2Index == 2)) or ((arg1Index == 2) and (arg2Index == 1)):
        return 0
    elif ((arg1Index == 0) and (arg2Index == 2)) or ((arg1Index == 2) and (arg2Index == 0)):
        return 1
    else:
        # If it wasn't found, return -1
        return -1


def getOrientation(args):
    # The only valid axes are x, y, and z
    VALID_VALUES = ["x", "y", "z"]
    
    # If only one axis is specified, that is the bottom axis, and the next letters in
    # line take the side then depth axes. 
    if (len(args) == 3) and (args[2] in VALID_VALUES):
        if (args[2] == "x"):
            return ("x", "y", "z")
        elif (args[2] == "y"):
            return ("y", "z", "x")
        elif (args[2] == "z"):
            return ("z", "x", "y")

    # If two are specified, find the axes which goes unspecified and make that the depth axis
    elif (len(args) == 4) and (args[2] in VALID_VALUES) and (args[3] in VALID_VALUES):
        # Check for duplicate axes
        if (args[2] == args[3]):
            raise ValueError("The same axis cannot be used more than once.")
        
        thirdIndex = findUnusedThird(args[2], args[3], VALID_VALUES)
        # If the third value's index wasn't found, throw an error
        if (thirdIndex == -1):
            raise ValueError("An error occured with setting the orientation.")
        
        # Return with the found third axis
        return (args[2], args[3], VALID_VALUES[thirdIndex])
    
    # If all three are specified, make that the orientation
    elif (len(args) > 4) and (args[2] in VALID_VALUES) and (args[3] in VALID_VALUES) and (args[3] in VALID_VALUES):
        # Since duplicates are ignored in sets, if the set length ends up as less than 3, 
        # it means one of the items was a duplicate, so throw an error
        if not (len({args[2], args[3], args[4]}) == 3):
            raise ValueError("The same axis cannot be used more than once.")
        
        return (args[2], args[3], args[4])

    # If an issue was encountered or none was specified, set orientation to default
    return ("x", "y", "z")


if (len(sys.argv) > 1):
    # If a command line argument is given, use that file
    mapFile = sys.argv[1]
else:
    # Get user input of what text file to read
    mapFile = input("Enter the name of the text file to read: ")


try: 
    # Get the orientation to display
    orientation = getOrientation(sys.argv)

    # Print a confirmation message
    print("Generating map with file " + mapFile + " and orientation " + str(orientation) + ".")

    # Get starmap information
    starmapInfo = getStarInfo(mapFile, orientation)

    # Draw board items
    map = createBoard(starmapInfo)
except Exception as e:
    # Show any errors
    print("Fatal Error: " + str(e))
else: 
    # Save the map
    saveImage(map)
