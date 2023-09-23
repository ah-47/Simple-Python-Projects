from PIL import Image

# Open th image file
image = Image.open("Guns.jpg")

# Define the new size (width, height)
new_size = (500, 500)

# Resize the image
resized_image = image.resize(new_size)

# Save the resized image to a file
resized_image.save("resized_image.jpg")

# Display the image using the default image viewer
resized_image.show()

# Close the original and resized images
# image.close()
# resized_image.close()