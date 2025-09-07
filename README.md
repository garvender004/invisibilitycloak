# Invisibilitycloak
Building a software to replicate the invisibility cloack of Harry Potter Movie using python , opencv and numpy .

🔍 How it Works
Background Capture: First, the program captures the static background without the person.
Color Detection (HSV Space): Using color thresholding in the HSV color space, the program identifies pixels corresponding to the chosen cloak color.
Masking & Segmentation: These cloak regions are masked and replaced with the previously captured background.
Final Output: The cloak blends with the background, creating the illusion of invisibility while the rest of the person remains visible.
🛠️ Technologies Used
Python – for coding the logic
OpenCV – for image processing and real-time computer vision
NumPy – for handling pixel arrays efficiently
