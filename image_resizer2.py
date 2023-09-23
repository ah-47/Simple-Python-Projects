import cv2 as cv

# Read the file
image = cv.imread("Guns.jpg")

# New Size (width, height)
new_size = (600, 600)

# Resized the image
resized_image = cv.resize(image, new_size)

# Save the resized image
cv.imwrite('resized_image1.jpg', resized_image)

# Show the image
cv.imshow('Image', resized_image)

# Wait for a key press and then close the window
cv.waitKey(0)
cv.destroyAllWindows()