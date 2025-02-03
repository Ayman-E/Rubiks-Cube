# class edge:
#     def __init__(self, c1):
#         self.c1 = c1

# class edge:
#     def __init__(self, c1,c2):
#         self.c1 = c1
#         self.c2 = c2

# class corner:
#     def __init__(self, c1,c2,c3):
#         self.c1 = c1
#         self.c2 = c2
#         self.c3 = c3
# Array to hold the current colors on the different sides
# Options are: Y,B,W,O,Bl,A
# Ordered 0-8, from top left to bottom right, 4 is the center piece
# 0 1 2
# 3 4 5
# 6 7 8
# Blue side facing you, white on top
# step 7: R U R' F' SPICY R' F R2 U' R', yellow top 
# step 8: M2 U' M' U'2 M U' M2

# From solved:
# U, then turn everything 360, front right back left
yellow = ['Y','W','W','W','Y','W','Y','W','W']
blue = ['O','B','A','B','B','A','B','O','Bl']
white = ['W','Y','Y','Y','W','Y','W','Y','Y']
orange = ['O','O','Bl','O','O','Bl','A','A','B']
black = ['A','Bl','B','O','Bl','Bl','O','B','Bl']
aqua = ['A','A','O','A','A','B','Bl','Bl','B']

front = blue
top = white
bottom = yellow

def setCube():
    temp = input("Blue Input: ")

    pass

def printSide(list):
    print(list[0] + " " + list[1] + " " + list[2])
    print(list[3] + " " + list[4] + " " + list[5])
    print(list[6] + " " + list[7] + " " + list[8] + "\n")

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

#Clockwise turn of front face
def F(front):
    #Rotates front side
    front[:] = [front[6], front[3], front[0], 
             front[7], front[4], front[1], 
             front[8], front[5], front[2]]
    
    # Makes a copy of the left side
    left = prevSide(front,white)
    right = nextSide(front,white)
    tempLeft = left[:]

    # Rotates the sides of the front
    left[2:9:3] = yellow[0:3]
    yellow[0:3] = right[0:7:3][::-1]
    right[0:7:3] = white[6:9]
    white[6:9] = tempLeft[8:1:-3]


def whiteCross():
    F(orange)
    #F(front)
    pass

printSide(aqua)
whiteCross()
printSide(aqua)


