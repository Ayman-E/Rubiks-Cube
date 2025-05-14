import cv2
import numpy as np

# Load camera
cam = cv2.VideoCapture(0)

# Define window
cv2.namedWindow('Camera')

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

blue = []
orange = []
green = []
pink = []
yellow = []
white = []

output = [blue,orange,green,pink,yellow,white]

def color(hsv):
    h, s, v = hsv

    if 93 <= h <= 113 and s > 100:
        return 'B'  # Blue
    elif 0 <= h <= 12:
        return 'O'  # Orange
    elif 38 <= h <= 70:
        return 'G'  # Green (Aqua)
    elif 145 <= h <= 175:
        return 'P'  # Pink (Black)
    elif 13 <= h <= 37:
        return 'Y'  # Yellow
    elif 71 <= h <= 150 and s < 75:
        return 'W'  # White
    else:
        return '?'  # Unknown color


def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for curColor in output: 
            for x2, y2 in points:
                currHSV = hsv_frame[y2, x2]
                curTile = color(currHSV)
                # print(f"HSV at ({x2},{y2}): {currHSV} => {curTile}")
                curColor.append(curTile)
            # print("-"*50)


cv2.setMouseCallback('Camera', pick_color)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame,(125,150),(400,450),(255,255,255),2)

    for x, y in points:
        cv2.rectangle(frame, (x, y), (x + 1, y + 1), (0, 0, 255), 1)

    cv2.imshow('Camera', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
