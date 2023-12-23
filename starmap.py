from reader import getStarInfo
from draw import createBoard, saveImage
import sys


if (len(sys.argv) > 1):
    # If a command line argument is given, use that file
    mapFile = sys.argv[1]
else:
    # Get user input of what text file to read
    mapFile = input("Enter the name of the text file to read: ")

try: 
    print("Generating map with file " + mapFile + ".")

    # Get starmap information
    starmapInfo = getStarInfo(mapFile)

    # Draw board items
    map = createBoard(starmapInfo)
except Exception as e:
    # Show any errors
    print("Fatal Error: " + str(e))
else: 
    # Save the map
    saveImage(map)
