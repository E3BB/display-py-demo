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

