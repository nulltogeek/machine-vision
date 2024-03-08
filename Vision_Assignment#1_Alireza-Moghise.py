import cv2
import numpy as np
import matplotlib.pyplot as plt


class MonochromeImage:
    def __init__(self, image):
        self.image = image
        self.blue_channel, self.green_channel, self.red_channel = cv2.split(self.image)
        self.titles = ["Red", "Green", "Blue"]
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

        axes[0].imshow(cv2.cvtColor(self.colors_monochrome[0], cv2.COLOR_BGR2RGB))
        axes[0].set_title(self.titles[0])

        axes[1].imshow(cv2.cvtColor(self.colors_monochrome[1], cv2.COLOR_BGR2RGB))
        axes[1].set_title(self.titles[1])

        axes[2].imshow(cv2.cvtColor(self.colors_monochrome[2], cv2.COLOR_BGR2RGB))
        axes[2].set_title(self.titles[2])

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
