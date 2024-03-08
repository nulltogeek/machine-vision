import cv2
import numpy as np
import matplotlib.pyplot as plt


def monochrome_image(image):
    blue_channel, green_channel, red_channel = cv2.split(image)

    red_monochrome = np.zeros_like(image)
    red_monochrome[:, :, 2] = red_channel

    green_monochrome = np.zeros_like(image)
    green_monochrome[:, :, 1] = green_channel

    blue_monochrome = np.zeros_like(image)
    blue_monochrome[:, :, 0] = blue_channel

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    axes[0].imshow(cv2.cvtColor(red_monochrome, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Red Channel")

    axes[1].imshow(cv2.cvtColor(green_monochrome, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Green Channel")

    axes[2].imshow(cv2.cvtColor(blue_monochrome, cv2.COLOR_BGR2RGB))
    axes[2].set_title("Blue Channel")

    for ax in axes:
        ax.axis("off")

    plt.tight_layout()
    plt.show()
    return red_monochrome, green_monochrome, blue_monochrome

 
monochrome_image(cv2.imread("test.jpg"))