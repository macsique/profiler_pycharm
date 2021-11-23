import os
import numpy as np
from PIL import Image, UnidentifiedImageError

STANDARD_PIXEL_SIZE = 10
STANDARD_GRAYSCALE = 50


def load_img_as_array(path: str) -> np.ndarray:
    if os.path.isfile(path):
        try:
            img = Image.open(path)
            return np.array(img)
        except UnidentifiedImageError:
            print("Incorrect file type.")
            exit(1)
    print("This file doesn't exist.")
    exit(1)


def convert_to_gray_pixel_art(img: np.ndarray, pixel_size: int = STANDARD_PIXEL_SIZE,
                              grayscale: int = STANDARD_GRAYSCALE) -> np.ndarray:
    for x in range(0, len(img), pixel_size):
        for y in range(0, len(img[0]), pixel_size):
            brightness = np.average(img[x: x + pixel_size, y: y + pixel_size])
            img[x: x + pixel_size, y: y + pixel_size] = brightness - brightness % grayscale

    return img


def save_img(img: np.ndarray, filename: str) -> None:
    Image.fromarray(img).save(filename)


def convert(input_path: str, output_path: str = None, pixel_size: int = STANDARD_PIXEL_SIZE,
            grayscale: int = STANDARD_GRAYSCALE) -> None:
    img = load_img_as_array(input_path)
    gray_image = convert_to_gray_pixel_art(img, pixel_size, grayscale)
    file_info = os.path.splitext(input_path)
    output_path = output_path or f"{file_info[0]}_pixel{file_info[1]}"
    save_img(gray_image, output_path)


def main() -> None:
    convert("img.jpg")


if __name__ == "__main__":
    main()
