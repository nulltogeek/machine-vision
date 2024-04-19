import cv2
import numpy as np
import matplotlib.pyplot as plt


class ImageHistogram:
    def __init__(self, image_path):
        self.image_path = image_path
        self.color_image = None
        self.gray_image = None
        self.hist_ready = None
        self.hist_manual = None

    def load_image(self):

        self.color_image = cv2.imread(self.image_path)

    def convert_to_gray(self):

        self.gray_image = cv2.cvtColor(self.color_image, cv2.COLOR_BGR2GRAY)

    def calculate_histograms(self):

        self.hist_ready = cv2.calcHist(
            [self.gray_image], [0], None, [256], [0, 256]
        ).flatten()


        self.hist_manual = np.zeros(256)
        for i in range(self.gray_image.shape[0]):
            for j in range(self.gray_image.shape[1]):
                self.hist_manual[self.gray_image[i, j]] += 1

    def plot_histograms(self):

        fig, axs = plt.subplots(1, 2, figsize=(20, 5))


        axs[0].set_title("Histogram - Ready Function")
        axs[0].set_xlabel("Pixel value")
        axs[0].set_ylabel("Frequency")
        axs[0].bar(range(256), self.hist_ready, color="blue")


        axs[1].set_title("Histogram - Manual Method")
        axs[1].set_xlabel("Pixel value")
        axs[1].set_ylabel("Frequency")
        axs[1].bar(range(256), self.hist_manual, color="red", alpha=0.5)


        plt.tight_layout()
        plt.show()



image_histogram = ImageHistogram("test.jpg")
image_histogram.load_image()
image_histogram.convert_to_gray()
image_histogram.calculate_histograms()
image_histogram.plot_histograms()
