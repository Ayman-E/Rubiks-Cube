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
    print(list[6] + " " + list[7] + " " + list[8])

def nextSide(color):
    if(color == blue):
        return orange
    elif (color == orange):
        return aqua
    elif (color == aqua):
        return black
    elif (color == black):
        return blue
    elif (color == white):
        return yellow
    else:
        return white

def D():
    #Rotates yellow side
    yellow[:] = [yellow[6], yellow[3], yellow[0], 
             yellow[7], yellow[4], yellow[1], 
             yellow[8], yellow[5], yellow[2]]
    
    #Rotates the bottom 3 pieces of each side
    tempBlue = blue[:]
    blue[6:9] = black[6:9]
    black[6:9] = aqua[6:9]
    aqua[6:9] = orange[6:9]
    orange[6:9] = tempBlue[6:9]


def whiteCross():

    pass

printSide(black)
D()
print("")
printSide(black)


