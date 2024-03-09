import cv2
import numpy as np
import matplotlib.pyplot as plt


class MonochromeImage:
    def __init__(self, image):
        self.image = image

        # intensity values
        self.blue_channel, self.green_channel, self.red_channel = cv2.split(self.image)
        self.titles = ["Blue", "Green", "Red"]
        self.colors_monochrome = []

    def monochrome_red(self):
        red_monochrome = np.zeros_like(self.image)
        red_monochrome[:, :, 2] = self.red_channel
        self.colors_monochrome.append(red_monochrome)
        return red_monochrome

    def monochrome_green(self):
        green_monochrome = np.zeros_like(self.image)
        green_monochrome[:, :, 1] = self.green_channel
        self.colors_monochrome.append(green_monochrome)
        return

    def monochrome_blue(self):
        blue_monochrome = np.zeros_like(self.image)
        blue_monochrome[:, :, 0] = self.blue_channel
        self.colors_monochrome.append(blue_monochrome)
        return

    def show(self):
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))

        for i in range(3):
            axes[i].imshow(cv2.cvtColor(self.colors_monochrome[i], cv2.COLOR_BGR2RGB))
            axes[i].set_title(self.titles[i])

        for ax in axes:
            ax.axis("off")

        plt.tight_layout()
        plt.show()
        return (
            self.colors_monochrome[0],
            self.colors_monochrome[1],
            self.colors_monochrome[2],
        )


monochrome = MonochromeImage(cv2.imread("test.jpg"))
monochrome.monochrome_blue()
monochrome.monochrome_red()
monochrome.monochrome_green()
monochrome.show()
