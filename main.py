# Display module - Elliott

display = list # To access given cell after filling, do display[y][x]
dispx = 16
dispy = 9
blank_letter = "I"

def wipe_display():
    global display # Global used b/c otherwise display is diff local var, and lin15 applies to loc var not glob var
    display = []
    for i in range(dispy):
        new_arr = []
        for o in range(dispx):
            new_arr.append(blank_letter + " ") # + " " b/c norm disp = NNNN, but w/ spc = N N N N
        display.append([x for x in new_arr]) # Appends new_arr to (end of) disp.x

def print_display():
    for y_buffer in display:
        new_line = ""
        for x in y_buffer:
            new_line = new_line + x
        print(new_line)
    print()

def change_pixel(x:int, y:int, char:str):
    if x<0: x=0 # X-value checks
    elif x>(dispx-1): x=dispx-1
    
    if y<0: y=0 # Y-value checks
    elif y>(dispy-1): y=dispy-1

    if len(char) > 1: print("Char too long; new char is ", char[0])
    char = char[0] # Sets character to only first value
    
    display[y][x] = char + " " # Sets cell to character
    # P.S. global does not have to be used b/c array inside array is basically global

wipe_display()
change_pixel(3,2,"A")
print_display()
wipe_display()
print_display()
