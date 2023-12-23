# Traveller's Star Maps	
A simple Python application to generate visual starmaps for use in the TTRPG Traveller. 



## Python Libraries
This project utilizes the following Python libraries: 

* Pillow
* math
* mathplotlib
* sys
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

Valid color options are blue, brown, green, orange, purple, red, white, and yellow. Any invalid color will be set to white instead. 



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


# Usage
Open the command line and run `starmap.py`. When starting the program, it will ask for a filename. Input the path to a text file that has been formatted to the above specifications. The program will generate an image according to that text file and store it in an `output` folder located in the same directory as the script. The text file name can also be included as a command line argument. 

### Orientation
When using the command line, the user may specify the orientation of the map. All stars have an x, y, and z value which are the second, third, and fourth values specified on each line of the text file respectively. When working on the command line, after the filename, the user may enter these axes to determine how the map is rendered. The first axis is the horizontal axis, the second is the vertical, and the third is the depth axis. 

When a single axis is entered, it will be the horizontal axis, with the other two automatically assinged in alphabetical order after it. Entering
```
python starmap.y test.txt y
```
will result in an orientation of (y, z, x). 

When two axes are entered, the third is automatically assigned as the depth axis. Entering
```
python starmap.py test.txt z x
```
will result in an orientation of (z, x, y). 

Entering all three will use that orientation. Entering 
```
python starmap.py test.txt z y x
```
will result in an orientation of (z, y, x). 

If there is an error with this, such as entering the same axis twice or entering a value which is not x, y, or z, the program will simply default to using (x, y, z). 