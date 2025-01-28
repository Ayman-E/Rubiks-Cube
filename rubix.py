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

def setCube():
    temp = input("Blue Input: ")

    pass

def printSide(list):
    print(list[0] + " " + list[1] + " " + list[2])
    print(list[3] + " " + list[4] + " " + list[5])
    print(list[6] + " " + list[7] + " " + list[8])


def whiteCross():
    pass

printSide(blue)

