import matplotlib.pyplot as plt

def show_imagesmpl(*images):
    num_images = len(images)
    fig, axes = plt.subplots(1, num_images, figsize=(15, 5))
    for i in range(num_images):
        axes[i].imshow(images[i])
        axes[i].axis('off')
    plt.show()

# Example usage:
# Assuming you have two images img1 and img2
# You can call the function like this:
# show_images_side_by_side(img1, img2)

import cv2 as cv
import numpy as np

def show_imagescv(*images):
    # Resize images to have the same dimensions
    max_height = max(image.shape[0] for image in images)
    max_width = max(image.shape[1] for image in images)
    
    resized_images = []
    for image in images:
        resized_image = cv.resize(image, (max_width, max_height))
        resized_images.append(resized_image)
    
    # Concatenate images horizontally
    concatenated_image = np.concatenate(resized_images, axis=1)
    
    # Show the concatenated image
    cv.imshow("Images Side by Side", concatenated_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
