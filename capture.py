from PIL import ImageGrab

# Define the coordinates of the area to capture
left = 320
top = 432
right = 541
bottom = 541

import time
time.sleep(2)
# Capture the image
im = ImageGrab.grab(bbox=(left, top, right, bottom))

# Save the image
im.save("captured_image.png")