from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
import math

from reader import getStarInfo
from draw import createBoard



# Get starmap information
starmapInfo = getStarInfo()

# Draw board items
map = createBoard(starmapInfo)

# Show the map
map.show()
