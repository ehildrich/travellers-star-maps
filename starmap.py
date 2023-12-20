from reader import getStarInfo
from draw import createBoard


# Get user input of what text file to read
mapFile = input("Enter the name of the text file to read: ")

# Get starmap information
starmapInfo = getStarInfo(mapFile)

# Draw board items
map = createBoard(starmapInfo)

# Show the map
map.show()
