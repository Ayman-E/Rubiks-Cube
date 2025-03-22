import random
# step 7: R U R' F' SPICY R' F R2 U' R', yellow top 
# step 8: M2 U' M' U'2 M U' M2

# Array to hold the current colors on the different sides
# Options are: (Y)ellow,(B)lue,(W)hite,(O)range,(Bl)ack,(A)qua
# Ordered 0-8, from top left to bottom right, 4 is the center piece
# 0 1 2
# 3 4 5
# 6 7 8
# Below is the array filled with a solved cube

yellow = ['Y','Y','Y','Y','Y','Y','Y','Y','Y']
blue = ['B','B','B','B','B','B','B','B','B']
white = ['W','W','W','W','W','W','W','W','W']
orange = ['O','O','O','O','O','O','O','O','O']
black = ['Bl','Bl','Bl','Bl','Bl','Bl','Bl','Bl','Bl']
aqua = ['A','A','A','A','A','A','A','A','A']

# Array to hold the steps taken to solve the cube
steps = []
# Format: Move: (F)ront / (T)op

# Function to set the cubes arrays
# Eventually will use a camera and learn to use computer vision to set the cube
def setCube():
    temp = input("Blue Input: ")

    pass

# Scrambles the cube randomly, used for testing
def scrambleCube(n):
    tops = [white,yellow]
    sides = [blue,orange,aqua,black]
    for _ in range(n):
        F(random.choice(sides))
        D(random.choice(tops))

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

#Returns true if the white corner is aligned correctly
def alignedPiece(color1,color2,corner):
    cornerMap = {
        "B": 6,  # Blue Black Corner
        "O": 8,  # Orange Blue Corner
        "A": 2,  # Aqua Orange Corner
        "Bl": 0  # Black Aqua Corner
    }

    # If checking a corner
    if (corner):
        return (
            color1[0] == color1[4] and 
            color2[2] == color2[4] and 
            white[cornerMap.get(color1[4], -1)] == "W"
        )
    else:
        # If checking an edge
        return (
            color1[3] == color1[4] and 
            color2[5] == color2[4]
        )


# Checks if the white corner piece is in the correct spot, can check the bottom and top face
def correctCornerSpot(color1,color2,direction):
    cornerMapWhite = {
        "B": 6,  # Blue Black Corner
        "O": 8,  # Orange Blue Corner
        "A": 2,  # Aqua Orange Corner
        "Bl": 0  # Black Aqua Corner
    }

    cornerMapYellow = {
        "B": 0,  # Blue Black Corner
        "O": 2,  # Orange Blue Corner
        "A": 8,  # Aqua Orange Corner
        "Bl": 6  # Black Aqua Corner
    }

    myList = []
    # If direction is true then it checks the bottom white side, otherwise it checks the top yellow side
    if (direction):
        myList.append(color1[0])
        myList.append(color2[2])
        myList.append(white[cornerMapWhite.get(color1[4], -1)])
    else:
        myList.append(color1[6])
        myList.append(color2[8])
        myList.append(yellow[cornerMapYellow.get(color1[4], -1)])
    
    return (
        color1[4] in myList and 
        color2[4] in myList and 
        "W" in myList
    )

# Checks the white corners to see if the inputed corner piece is in the bottom, if it is, it moves it to the yellow side
def correctCornerPiece(color1,color2):
    cornerMap = {
        "B": 6,  # Blue Black Corner
        "O": 8,  # Orange Blue Corner
        "A": 2,  # Aqua Orange Corner
        "Bl": 0  # Black Aqua Corner
    }   


    myList = []
    myList.append(color1[4])
    myList.append(color2[4])
    myList.append("W")
    count = 0

    faces = [color2,nextSide(color2,yellow)]
    faces.append(nextSide(faces[1],yellow))
    faces.append(color1)
    while count < 3:
        if (faces[count][0] in myList and faces[count+1][2] in myList and white[cornerMap.get(faces[count][4], -1)] in myList) == True:
            FPrime(faces[count])
            D(yellow)
            F(faces[count])
            return
        count += 1

# Puts the inputted corner from the yellow side to its correct spot in the corresponding white corner
def putInCorner(color1,color2):
    while correctCornerSpot(color1,color2,False) == False:
        D(yellow)

    while alignedPiece(color1,color2,True) == False:
        rSpicy(color1,yellow) 

# Checks if an edge piece is in the wrong spot/orientation in the second layer
def incorrectEdgePiece(color1, color2):
    myList = [color1[4], color2[4]]

    faces = [color1, color2, nextSide(color2, yellow),prevSide(color1, yellow),color1]

    count = 0
    while count < 4:
        # Check if the edge piece is in the wrong spot or orientation
        if (faces[count][3] in myList and faces[count+1][5] in myList) == True:
            # Moves the piece to the top layer
            rSpicy(faces[count], yellow)
            lSpicy(faces[count+1],yellow)
            return
        else:   count += 1

# Puts the inputted edge from the yellow side to its correct spot
def putInEdge(color1,color2):
    # Map for the position above the edge piece on each yellow side
    edgeMap = {
        "B": 1, 
        "O": 5,  
        "A": 7, 
        "Bl": 3  
    }   
    count = 0
    while count < 4:
        # If the color of the edge piece on the face is color1 it will do this, otherwise it will do the else if
        if(color1[7] == color1[4] and yellow[edgeMap.get(color1[4],-1)] == color2[4]):
            D(yellow)
            rSpicy(color1,yellow)
            lSpicy(color2,yellow)
            return
        elif (color2[7] == color2[4] and yellow[edgeMap.get(color2[4],-1)] == color1[4]):
            DPrime(yellow)
            lSpicy(color2,yellow)
            rSpicy(color1,yellow)
            return
        else:
            D(yellow)
            count += 1
        
# Following function returns which side is the front for the yellow cross step
# It returns a value representing which case we are on
def whichCase():
    # If it is already a yellow cross
    if (yellow[1] == "Y" and yellow[3] == "Y" and
        yellow[5] == "Y" and yellow[7] == "Y"):
        return blue, 0 #Arbitrary side, doesn't matter
    
    # If it is the yellow line, two cases of how it could look
    if (yellow[3] == "Y" and yellow[5] == "Y"): # Horizontol (If Blue side facing away from you)
        return blue, 1 #Either Blue or Aqua side work
    elif (yellow[1] == "Y" and yellow[7] == "Y"): # Vertical (If Blue side facing away from you)
        return orange, 1 #Either Orange or Black side work

    # If it is the half cross, four cases for each side
    if (yellow[1] == "Y" and yellow[3] == "Y"):
        return aqua,2
    elif (yellow[1] == "Y" and yellow[5] == "Y"):
        return black, 2
    elif (yellow[5] == "Y" and yellow[7] == "Y"):
        return blue, 2   
    elif (yellow[7] == "Y" and yellow[3] == "Y"):
        return orange, 2

    #If we are here, then that means we have just the yellow dot
    #We want to do F Rspicy F' then call this function again
    F(blue) #Arbitrary color, doesn't matter
    rSpicy(blue,yellow)
    FPrime(blue)    
    return whichCase()

# Following function returns which side (if any) are chest plates, rotates it to be in the chestplate
def whichChest():
    colors = [blue,black,aqua,orange]
    count = 0
    myList = []
    temp = "X"
    for curColor in colors:
        if (curColor[6] == curColor[8]): #If these two are the same then we know its a chest plate
            count += 1
            temp = curColor[6]
            # while (curColor[6] != curColor[4]):
            #     D(yellow)
    if (temp != "X"):
        for curColor in colors:
            if curColor[4] == temp:
                myList.append(curColor)
                while (curColor[6] != curColor[4]):
                    D(yellow)


    return myList,count

# Returns true if the cube is complete, otherwise false
def cubeDone():
    colors = [blue,black,aqua,orange]
    for curColor in colors:
        if all(i == curColor[4] for i in curColor) == False:
            return False
    return True
    

#Following functions are all Rubix cube moves, a png is provided to provide a visual

#Clockwise turn of bottom side
def D(bottom):
    #Rotates bottom side
    bottom[:] = [bottom[6], bottom[3], bottom[0], 
             bottom[7], bottom[4], bottom[1], 
             bottom[8], bottom[5], bottom[2]]
    
    if(bottom == yellow):
        #Makes a copy of the front side
        tempFront = blue[:]

        #Rotates the bottom 3 pieces of each side
        temp = prevSide(blue,white)
        blue[6:9] = temp[6:9]
        temp2 = prevSide(temp,white) 
        temp[6:9] = temp2[6:9]
        temp = prevSide(temp2,white) 
        temp2[6:9] = temp[6:9]
        temp[6:9] = tempFront[6:9]
        steps.append('D:W')
    else: #If the bottom side is the white side
        #Makes a copy of the front side
        tempFront = blue[:]

        #Rotates the bottom 3 pieces of each side
        temp = prevSide(blue,yellow)
        blue[0:3] = temp[0:3]
        temp2 = prevSide(temp,yellow) 
        temp[0:3] = temp2[0:3]
        temp = prevSide(temp2,yellow) 
        temp2[0:3] = temp[0:3]
        temp[0:3] = tempFront[0:3]
        steps.append('D:Y')

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
        steps.append('F:B')  
    elif color == 1: #orange
        left[2:9:3] = yellow[2:9:3]
        yellow[2:9:3] = right[0:7:3][::-1]
        right[0:7:3] = white[2:9:3][::-1]
        white[2:9:3] = tempLeft[8:1:-3][::-1]
        steps.append('F:O')  
    elif color == 2: #aqua
        left[2:9:3] = yellow[6:9][::-1]
        yellow[6:9] = right[0:7:3]
        right[0:7:3] = white[0:3][::-1]
        white[0:3] = tempLeft[8:1:-3][::-1]
        steps.append('F:A')  
    else:#black
        left[2:9:3] = yellow[0:7:3][::-1]
        yellow[0:7:3] = right[0:7:3]
        right[0:7:3] = white[0:7:3]
        white[0:7:3] = tempLeft[8:1:-3]
        steps.append('F:Bl')  

# Moves the middle layer up, only use case is when yellow is on top
def M(front):
    tempFront = front[:]

    if front == blue:
        front[1:8:3] = white[1:8:3]
        white[1:8:3] = aqua[1:8:3][::-1]
        aqua[1:8:3] = yellow[1:8:3][::-1]
        yellow[1:8:3] = tempFront[1:8:3]
    elif front == orange:
        front[1:8:3] = white[3:6:1]
        white[3:6:1] = black[1:8:3][::-1]
        black[1:8:3] = yellow[3:6:1]
        yellow[3:6:1] = tempFront[1:8:3][::-1]
    elif front == black:
        front[1:8:3] = white[3:6:1]
        white[3:6:1] = orange[1:8:3][::-1]
        orange[1:8:3] = yellow[3:6:1][::-1]
        yellow[3:6:1] = tempFront[1:8:3]
    else: #Front == aqua
        front[1:8:3] = white[1:8:3][::-1]
        white[1:8:3] = blue[1:8:3]
        blue[1:8:3] = yellow[1:8:3]
        yellow[1:8:3] = tempFront[1:8:3][::-1]

#Move middle down
def MPrime(front):
    M(front)
    M(front)
    M(front)

#Anticlockwise turn of bottom side
def DPrime(top):
    D(top)
    D(top)
    D(top)

#AntiClockwise turn of front face
def FPrime(front):
    F(front)
    F(front)
    F(front)

#Moving right column up
def R(front,top):
    F(nextSide(front,top))

#Moving right column down
def RPrime(front,top):
    FPrime(nextSide(front,top))

#Moving top left
def U(top):
    D(top)

#Moving top right
def UPrime(top):
    U(top)
    U(top)
    U(top)

#Right spicy is moving right side up, then top left, then right down, then top right
def rSpicy(front, top):
    R(front,top)
    U(top)
    RPrime(front,top)
    UPrime(top)

#Pretty much a right spicy but on the other side
def lSpicy(front, top):
    oppositeSide = prevSide(prevSide(front,top),top)
    RPrime(oppositeSide,top)
    UPrime(top)
    R(oppositeSide,top)
    U(top)
    
# The following functions are all the steps needed to solve the cube
# They are in order, they assume that the previous function has been ran correctly

# Yellow daisy
def yellowDaisy():
    sides = [blue,orange,aqua, black]

    edgeMap = {
        "B": 1,  # Blue Yellow Edge
        "O": 5,  # Orange Yellow Edge
        "A": 7,  # Aqua Yellow Edge
        "Bl": 3  # Black Yellow Edge
    }
    while (yellow[1] != "W" or yellow[3] != "W" or yellow[5] != "W" or yellow[7] != "W"):
        # Checks white side
        for _ in range(4):
                if white[5] == "W":
                    while(yellow[edgeMap.get(orange[4],-1)] == "W"):
                        D(yellow)
                    FPrime(orange)
                    FPrime(orange)
                U(white)
        
        for thisSide in sides:
            myNextSide = nextSide(thisSide,white)
            for _ in range(4):
                if thisSide[5] == "W":
                    while(yellow[edgeMap.get(myNextSide[4],-1)] == "W"):
                        D(yellow)
                    FPrime(myNextSide)
                F(thisSide)

# Solves the whtie cross, assumes a yellow daisy is made
def extendedWhiteCross():
    edgeMap = {
        "B": 1,  # Blue Yellow Edge
        "O": 5,  # Orange Yellow Edge
        "A": 7,  # Aqua Yellow Edge
        "Bl": 3  # Black Yellow Edge
    }
    sides = [blue,orange,aqua, black]
    for thisSide in sides:
        while (thisSide[4] != thisSide[7] or yellow[edgeMap.get(thisSide[4],-1)] != "W"):
            D(yellow)
        F(thisSide)
        F(thisSide)

# Solves the white corners, assumes an extended white cross is made
def whiteCorners():
    sides = [blue,orange,aqua, black]
    for thisSide in sides:
        myNextSide = nextSide(thisSide,yellow)
        if alignedPiece(thisSide,myNextSide,True) == False: #If its correct then don't do anything
            if correctCornerSpot(thisSide,myNextSide,True) == True: #If its in the right spot but wrong orientation then rSpicy until good
                while alignedPiece(thisSide,myNextSide,True) == False:
                    rSpicy(thisSide,yellow)
            else:
                # Wrong spot Cases:
                # 1. In the spot of someone elses corner
                # Following function moves the piece to the yellow top if its on the white bottom, otherwise does nothing
                correctCornerPiece(thisSide,myNextSide)

                # 2. At the top
                # Fololwing function moves the correct piece so that is aligned in the right spot, then puts it in

                putInCorner(thisSide,myNextSide)

# Solves the second layer
def secondLayer():
    sides = [blue,orange,aqua, black]
    for thisSide in sides:
        myNextSide = nextSide(thisSide,yellow)
        # Three Cases:
        # 1. The piece is in the correct spot
        # 2. The piece is in the 2nd layer somewhere
        # 3. The piece is in the yellow layer
        if alignedPiece(thisSide,myNextSide,False) == False: #If its correct then don't do anything
            # If it is in the second layer, then move it to the top, otherwise do nothing
            incorrectEdgePiece(thisSide,myNextSide)

            # Now the edge piece is somewhere at the top, this function inserts it
            putInEdge(thisSide,myNextSide)

# Solves the yellow cross
def yellowCross():
    # Four Cases:
    # 1. Just yellow middle dot
    # 2. Yellow Half cross
    # 3. Yellow line
    # 4. Yellow Cross
    # Need to detect which case I am currently on, getting from one case to the next is a simple combo
    whichSide, case = whichCase()
    
    # Now to run the algorithm
    F(whichSide)
    for _ in range(case):
        rSpicy(whichSide,yellow)
    FPrime(whichSide)

# Solves the yellow corners
def yellowCorners():
    # Simple algorithm that solves the four yellow corners
    for _ in range(4):
        while(yellow[2] != "Y"):
            rSpicy(blue,white)
        D(yellow)

# Solves the chestplates
def chestPlates():
    myList, numberOfChests = whichChest()

    if numberOfChests == 4: return #If it has four chests then do nothing
    elif numberOfChests == 1:
        # Following is the algorithm that needs to be ran
        # It needs to be ran with the chest plate in your left hand, yellow on top
        # R U R’ F’ (spicy) R’ F R2 U’ R’
        besideChest = nextSide(myList[0],yellow)
        R(besideChest,yellow)
        U(yellow)
        RPrime(besideChest,yellow)
        FPrime(besideChest)
        rSpicy(besideChest,yellow)
        RPrime(besideChest,yellow)
        F(besideChest)
        R(besideChest,yellow)
        R(besideChest,yellow)
        UPrime(yellow)
        RPrime(besideChest,yellow)

        #Now I have four chest plates, calling whichChest rotates it for me
        myList, numberOfChests = whichChest()
    else:
        # No chest plate, have to run algorithm on any side which gives one chest plate
        # Then do it again but with the chest plate
        R(blue,yellow)
        U(yellow)
        RPrime(blue,yellow)
        FPrime(blue)
        rSpicy(blue,yellow)
        RPrime(blue,yellow)
        F(blue)
        R(blue,yellow)
        R(blue,yellow)
        UPrime(yellow)
        RPrime(blue,yellow)
        chestPlates()

# This is the final step, it solves the cube completely
def solveAll():
    # Two cases, four chest plates, or 3 chest plates with one side
    colors = [blue,black,aqua,orange]
    for curColor in colors:
        if all(i == curColor[4] for i in curColor):
            oppositeSide = nextSide(nextSide(curColor,yellow),yellow)
            # Algorithm to do on oppositeSide of full face:
            # M2 U’ M’ U’2 M U’ M2
            while cubeDone() == False:
                M(oppositeSide)
                M(oppositeSide)
                UPrime(yellow)
                MPrime(oppositeSide)
                UPrime(yellow)
                UPrime(yellow)
                M(oppositeSide)
                UPrime(yellow)
                M(oppositeSide)
                M(oppositeSide)
            return
    #If I reach this point then I have 4 chest plates and need to run the algorithm on any color
    M(blue)
    M(blue)
    UPrime(yellow)
    MPrime(blue)
    UPrime(yellow)
    UPrime(yellow)
    M(blue)
    UPrime(yellow)
    M(blue)
    M(blue)
    solveAll()

# Function that solves the cube by calling all the steps in order, returns true if solved correctly, otherwise returns false
def solveMyCube():
    yellowDaisy()
    print("Yellow Daisy Done")
    extendedWhiteCross()
    print("Done extended")
    whiteCorners()
    print("Done white corner")
    secondLayer()
    print("Done second layer")
    yellowCross()
    print("Done yellow cross")
    yellowCorners()
    print("Done yellow corners")
    chestPlates()
    print("Done chest plates")
    solveAll()
    print("Done solved all")
    print(cubeDone())
    print("Number of steps:" + str(len(steps)))
    return cubeDone()

# Tests the algorithm 10000 random times
for _ in range(10000):
    scrambleCube(25) # Scrambles the cube
    if solveMyCube() == False: # Solves the cube
        print("Failed")
        break
    steps.clear()



