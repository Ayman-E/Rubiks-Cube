import cv2
import numpy as np

# Function to call from outside this file
# Uses a camera to read the colors of the cube and returns it as a list
# For the solving algorithm to use
def pickMyColor():
    exit = [False]
    output = []

    # Load camera
    cam = cv2.VideoCapture(0)

    # Define window
    cv2.namedWindow('Camera')

    # Set points where the cube will be aligned
    # Nine points for the 9 tiles on a cubes face
    points = [
    (170, 200),
    (270, 200),
    (370, 200),
    (170, 300),
    (270, 300),
    (370, 300),
    (170, 400),
    (270, 400),
    (370, 400)
    ]

    # Function that returns the character of the color detected for the list
    def color(hsv):
        h, s, v = hsv

        if 93 <= h <= 113 and s > 100:
            return 'B'  # Blue
        elif 0 <= h <= 12:
            return 'O'  # Orange
        elif 38 <= h <= 70:
            return 'A'  # Green (Aqua)
        elif 145 <= h <= 175:
            return 'Bl'  # Pink (Black)
        elif 13 <= h <= 37:
            return 'Y'  # Yellow
        elif 71 <= h <= 150 and s < 75:
            return 'W'  # White
        else:
            return '?'  # Unknown color

    # Function that is triggered when camera window is left clicked
    # Reads the colors of 9 points on the screen where the cube will be
    def pick_color(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            for x2, y2 in points:
                currHSV = hsv_frame[y2, x2]
                curTile = color(currHSV)
                # print(f"HSV at ({x2},{y2}): {currHSV} => {curTile}")
                output.append(curTile)
            # Sentinel value
            exit[0] = True

    # When clicked on the camera window it calls pick_color
    cv2.setMouseCallback('Camera', pick_color)

    # Continuously reads a frame from the camera
    while True:
        _, frame = cam.read()

        # Turns the captured frame into HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Draws a rectangle to align the cube
        cv2.rectangle(frame,(125,150),(400,450),(255,255,255),2)

        # Draws super small rectangles that show what points are being read
        for x, y in points:
            cv2.rectangle(frame, (x, y), (x + 1, y + 1), (0, 0, 255), 1)

        # Displays camera window
        cv2.imshow('Camera', frame)
        
        # Sentinel exit
        if exit[0] == True:
            break

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    # Returns the list with the colors
    return output
