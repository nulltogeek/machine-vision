import cv2
import numpy as np


class ImageResizer:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def resize_image(self, size):
        return cv2.resize(self.gray_image, (size, size))

    def resize_and_concatenate_images(self, sizes):
        resized_images = [self.resize_image(size) for size in sizes]
        resized_images = [cv2.resize(img, (480, 480)) for img in resized_images]
        concatenated_image = np.hstack(resized_images)
        return concatenated_image


resizer = ImageResizer("test.jpg")

sizes = [1024, 512, 32]

resized_concatenated = resizer.resize_and_concatenate_images(sizes)

cv2.imshow("Resized Images", resized_concatenated)

cv2.waitKey(0)
cv2.destroyAllWindows()
