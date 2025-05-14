import cv2
import numpy as np

# Load camera
cam = cv2.VideoCapture(0)

# Define window
cv2.namedWindow('Camera')

def color(hsv):
    h, s, v = hsv

    if 93 <= h <= 113 and 159 <= s <= 255 and 56 <= v <= 156:
        return 'B'  # Blue
    elif 0 <= h <= 17 and 157 <= s <= 255 and 136 <= v <= 236:
        return 'O'  # Orange
    elif 38 <= h <= 58 and 93 <= s <= 193 and 75 <= v <= 175:
        return 'G'  # Green
    elif 155 <= h <= 175 and 125 <= s <= 225 and 122 <= v <= 222:
        return 'P'  # Pink
    elif 11 <= h <= 31 and 130 <= s <= 230 and 106 <= v <= 206:
        return 'Y'  # Yellow
    elif 91 <= h <= 111 and 0 <= s <= 83 and 111 <= v <= 211:
        return 'W'  # White
    else:
        return '?'  # Unknown color




def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
#17  200, 270 208, 350 200
#170 300, 270 300, 350 300
#170 400, 260 400, 370 400
        for y2 in range(200,401,100):
            for x2 in range(170,371,100):
                currHSV = hsv_frame[y2, x2]
                print(color(currHSV))

cv2.setMouseCallback('Camera', pick_color)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame,(125,150),(400,450),(255,255,255),2)
    cv2.imshow('Camera', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
