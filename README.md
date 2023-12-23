# Traveller's Star Maps	
A simple Python application to generate visual starmaps for use in the TTRPG Traveller. It is currently in progress. 



## Python Libraries
This project utilizes the following Python libraries: 

* Pillow
* math
* mathplotlib
* os
* datetime



## Text File Format
In order for the stars and lines to be read in properly from the text file, the file must be in the following format:

> PARAMETER<br>
> Image Size: X<br>
> Edge Size: X<br>
> Line Width: X<br>
> Star Size: X<br>
> Circle Size: X<br>
> Font Size: X<br>
><br>
> STAR<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> ...<br>
><br>
> CONNECT<br>
> label1, label2, line_color, line_diameter<br>
> label1, label2, line_color, line_diameter<br>
> ...

Within each section, the items can be in any order. 



# Values
All stars are placed on a square plane which runs from -100 to 100 on all axes. Each star's x, y, and z value must be within this range. The diameter of stars, the width of individual lines, and the parameters Line Width, Star Size, Circle Size, and Font Size are all relative to this 200x200 plane. The only exceptions are the Image Size and Edge Size, which are in pixels. 

### Parameters
- **Image Size**: Controls the width and height of the main board in pixels. 
- **Edge Size**: Controls how large the edge of the image is in pixels. The edge displays the edge rules of the board that mark the center and halfway point of each axis. The total width/height of the image is the image size plus an edge on either side. 
- **Line Width**: Controls the minimum width of the lines used in the edge rules, the circles on each star, and the lines between stars. If a given line between two stars has a line width smaller than this, it will be set to this instead. Relative to the 200x200 grid. 
- **Star Size**: Controls the maximum size of stars. Star size ranges between 1 and the max size depending on its z-axis. Relative to the 200x200 grid. 
- **Circle Size**: Controls the diamteter of the cirlces that surround each star. Relative to the 200x200 grid. If it is smaller than the given Star Size, it will automatically be set to be slightly larger than it. If a star's given diameter is smaller than this, it will be set to this instead. 
- **Font Size**: Controls how large the text is. Relative to the 200x200 grid. 

All parameters are given a minimum value if the provided value is too low. 