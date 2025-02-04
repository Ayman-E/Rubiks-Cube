# step 7: R U R' F' SPICY R' F R2 U' R', yellow top 
# step 8: M2 U' M' U'2 M U' M2

# Array to hold the current colors on the different sides
# Options are: (Y)ellow,(B)lue,(W)hite,(O)range,(Bl)ack,(A)qua
# Ordered 0-8, from top left to bottom right, 4 is the center piece
# 0 1 2
# 3 4 5
# 6 7 8
# Below are some hard coded inital values for testing
# From solved:
# U, then turn everything 360, front right back left
yellow = ['Y','W','W','W','Y','W','Y','W','W']
blue = ['O','B','A','B','B','A','B','O','Bl']
white = ['W','Y','Y','Y','W','Y','W','Y','Y']
orange = ['O','O','Bl','O','O','Bl','A','A','B']
black = ['A','Bl','B','O','Bl','Bl','O','B','Bl']
aqua = ['A','A','O','A','A','B','Bl','Bl','B']

# Blue side facing you, white on top
front = blue
top = white
bottom = yellow

# Array to hold the steps taken to solve the cube
steps = ['']

# Function to set the cubes arrays
def setCube():
    temp = input("Blue Input: ")

    pass

# Neatly prints one side, used for troubleshooting
def printSide(list):
    print(list[0] + " " + list[1] + " " + list[2])
    print(list[3] + " " + list[4] + " " + list[5])
    print(list[6] + " " + list[7] + " " + list[8] + "\n")

# Neatly prints all sides, used for troubleshooting
def printAll():
    sidesNames = ['Blue', 'Orange', 'Aqua', 'Black', 'White', 'Yellow']
    sides = [blue,orange,aqua, black, white, yellow]
    for i in range(0,6):
        print(sidesNames[i])
        printSide(sides[i])
    print('--------------------------------')

# Returns the color to the right
def nextSide(color, thisTop):
    if(thisTop == white):
        if(color == blue):
            return orange
        elif (color == orange):
            return aqua
        elif (color == aqua):
            return black
        elif (color == black):
            return blue
    else:
        return prevSide(color, white)

# Returns the color to the left
def prevSide(color, thisTop):
    if(thisTop == white):
        if(color == blue):
            return black
        elif (color == black):
            return aqua
        elif (color == aqua):
            return orange
        elif (color == orange):
            return blue
    else:
        return nextSide(color, white)

#Following functions are all Rubix cube moves, a png is provided to provide a visual

#Clockwise turn of bottom side
def D(bottom):
    #Rotates bottom side
    bottom[:] = [bottom[6], bottom[3], bottom[0], 
             bottom[7], bottom[4], bottom[1], 
             bottom[8], bottom[5], bottom[2]]
    
    if(bottom == yellow):
        #Makes a copy of the front side
        tempFront = front[:]

        #Rotates the bottom 3 pieces of each side
        temp = prevSide(front,white)
        front[6:9] = temp[6:9]
        temp2 = prevSide(temp,white) 
        temp[6:9] = temp2[6:9]
        temp = prevSide(temp2,white) 
        temp2[6:9] = temp[6:9]
        temp[6:9] = tempFront[6:9]
    else: #If the bottom side is the white side
        #Makes a copy of the front side
        tempFront = front[:]

        #Rotates the bottom 3 pieces of each side
        temp = prevSide(front,yellow)
        front[0:3] = temp[0:3]
        temp2 = prevSide(temp,yellow) 
        temp[0:3] = temp2[0:3]
        temp = prevSide(temp2,yellow) 
        temp2[0:3] = temp[0:3]
        temp[0:3] = tempFront[0:3]

    steps.append('D')

#Clockwise turn of front face
def F(front):
    color = -1
    if front == blue:
        color = 0
    elif front == orange:
        color = 1
    elif front == aqua:
        color = 2
    else:#black
        color = 3

    #Rotates front side
    front[:] = [front[6], front[3], front[0], 
             front[7], front[4], front[1], 
             front[8], front[5], front[2]]
    
    # Makes a copy of the left side
    left = prevSide(front,white)
    right = nextSide(front,white)
    tempLeft = left[:]

    # Rotates the sides of the front
    if color == 0: #blue
        left[2:9:3] = yellow[0:3]
        yellow[0:3] = right[0:7:3][::-1]
        right[0:7:3] = white[6:9]
        white[6:9] = tempLeft[8:1:-3]
    elif color == 1: #orange
        left[2:9:3] = yellow[2:9:3]
        yellow[2:9:3] = right[0:7:3][::-1]
        right[0:7:3] = white[2:9:3]
        white[2:9:3] = tempLeft[8:1:-3][::-1]
    elif color == 2: #aqua
        left[2:9:3] = yellow[6:9][::-1]
        yellow[6:9] = right[0:7:3]
        right[0:7:3] = white[0:3][::-1]
        white[0:3] = tempLeft[8:1:-3][::-1]
    else:#black
        left[2:9:3] = yellow[0:7:3][::-1]
        yellow[0:7:3] = right[0:7:3]
        right[0:7:3] = white[0:7:3]
        white[0:7:3] = tempLeft[8:1:-3]
    
    steps.append('F')
    

# The following functions are all the steps needed to solve the cube
# They are in order, they assume that the previous function has been ran correctly

def whiteCross():
    sides = [blue,orange,aqua, black]
    for thisSide in sides:
        while thisSide[4] != thisSide[7]:
            D(yellow)
        F(thisSide)
        F(thisSide)

    
whiteCross()
printAll()


