# display-py-demo
This is python display demo. No modules are needed; just print(), for loops and nested arrays

## Function descriptions:
### wipe_display()
Initializes (or wipes) display. ***Always use this before other display functions!***

This function resets the current display, then refills it with the current 
blank_letter.

To change the display size, **change dispx and dispy before initializing
the display.**

### print_display()
Prints current display to terminal and adds a blank line.

Example:
```
L L L L
L L L L
L L L L

```
*Takes no values!*

### change_pixel(x,y,char)
Changes character in display at position of (x,y).

**Keep in mind, x/y values go from 0 to (display_size - 1)**;
*also char is string of length 1.*

Also, y=0 is top of display, y=dispy is bottom.
```
change_pixel(3,2,"j")
print_display()

I I I I
I I I I
I I I j
I I I I
```

## Variables
```
display = list
dispx = 16
dispy = 9
blank_letter = "I"
```

display is the list containing all rows of the display. The
pixels are stored as individual entries accessible by calling
```display[y][x]```, where y and x range from 0 to dispy and dispx
respectively. As well, the code makes use of how only first-tier objects
(non-nested obj's) are immutable (unchangeable), while nested objects in
a function are mutable (or smth like that; there's a whole lot of stuff
to comprehend about this).

dispx is the integer which defines how large the display is in the x
dimension. It cannot be less than or equal to 0.

dispy is the integer which defines how large the display is in the y
dimension. It cannot be less than or equal to 0.

blank_letter is a 1-length string which defines what value will be used
as the default character of the display. It can only be 1 character long.
