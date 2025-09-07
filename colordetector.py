import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Color Picker")

# Create trackbars with better defaults
cv2.createTrackbar("LH", "Color Picker", 120, 180, nothing)  # Start near purple hue
cv2.createTrackbar("LS", "Color Picker", 50, 255, nothing)
cv2.createTrackbar("LV", "Color Picker", 50, 255, nothing)
cv2.createTrackbar("UH", "Color Picker", 140, 180, nothing)
cv2.createTrackbar("US", "Color Picker", 255, 255, nothing)
cv2.createTrackbar("UV", "Color Picker", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar positions
    lh = cv2.getTrackbarPos("LH", "Color Picker")
    ls = cv2.getTrackbarPos("LS", "Color Picker")
    lv = cv2.getTrackbarPos("LV", "Color Picker")
    uh = cv2.getTrackbarPos("UH", "Color Picker")
    us = cv2.getTrackbarPos("US", "Color Picker")
    uv = cv2.getTrackbarPos("UV", "Color Picker")

    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # q or esc to quit
        print(f"Lower HSV: {lower}, Upper HSV: {upper}")
        break

cap.release()
cv2.destroyAllWindows()
