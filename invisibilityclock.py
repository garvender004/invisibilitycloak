import cv2
import numpy as np
import time

# --- Step 1: Open webcam ---
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not access the camera.")
    exit()

# Optional: set webcam resolution (HD)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

time.sleep(2)

# --- Step 2: Capture background ---
print("Stay out of the frame! Capturing background in 5 seconds...")
for i in range(5, 0, -1):
    print(f"Capturing in {i}...")
    time.sleep(1)

background = None
for i in range(30):
    ret, bg = cap.read()
    if ret and bg is not None:
        background = bg

if background is None:
    print("❌ Error: Could not capture background.")
    cap.release()
    exit()

background = np.flip(background, axis=1)
print("✅ Background captured! Wear purple to turn invisible...")

# --- Step 3: Cloak mode setup ---
cloak_mode = False  # invisibility toggle

# HSV range for purple (adjust if needed)
lower_purple = np.array([137, 0, 78])
upper_purple = np.array([180, 255, 248])

while True:
    ret, frame = cap.read()
    if not ret or frame is None or len(frame.shape) != 3:
        print("⚠️ Warning: Invalid frame. Skipping...")
        continue

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    if cloak_mode:
        # --- Apply invisibility effect for purple ---
        mask = cv2.inRange(hsv, lower_purple, upper_purple)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
        mask_inv = cv2.bitwise_not(mask)

        res1 = cv2.bitwise_and(background, background, mask=mask)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
        frame = cv2.addWeighted(res1, 1, res2, 1, 0)



    # --- Fullscreen window ---
    cv2.namedWindow("Invisibility Cloak", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Invisibility Cloak", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Invisibility Cloak", frame)

    # --- Controls ---
    key = cv2.waitKey(1) & 0xFF

    if key == ord('i'):  # invisibility ON
        cloak_mode = True

    elif key == ord('o'):  # invisibility OFF
        cloak_mode = False

    elif key == ord('q') or key == 27:  # quit
        break

cap.release()
cv2.destroyAllWindows()
