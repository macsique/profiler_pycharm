import argparse
import os
import numpy as np
from PIL import Image, UnidentifiedImageError

STANDARD_PIXEL_SIZE = 10
STANDARD_GRAYSCALE = 50

def load_img(path: str):
    if os.path.isfile(path):
        try:
            img = Image.open(path)
            return np.array(img)
        except UnidentifiedImageError:
            print("Incorrect file type.")
            exit(1)
    print("This file doesn't exist.")
    exit(1)


def conv_to_gray_pixel_art(img: np.ndarray, pixel_size: int = STANDARD_PIXEL_SIZE,
                              grayscale: int = STANDARD_GRAYSCALE):
    for x in range(0, len(img), pixel_size):
        for y in range(0, len(img[0]), pixel_size):
            brightness = np.average(img[x: x + pixel_size, y: y + pixel_size])
            img[x: x + pixel_size, y: y + pixel_size] = brightness - brightness % grayscale


    return img

def save_img(img: np.ndarray, filename: str):
    Image.fromarray(img).save(filename)



def convert(input_path: str, output_path: str = None, pixel_size: int = STANDARD_PIXEL_SIZE,
            grayscale: int = STANDARD_GRAYSCALE):
    img = load_img(input_path)
    gray_image = conv_to_gray_pixel_art(img, pixel_size, grayscale)
    file_info = os.path.splitext(input_path)
    output_path = output_path or f"{file_info[0]}_pixel{file_info[1]}"
    save_img(gray_image, output_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=str, help='Путь до входного изображения.')
    parser.add_argument('-op', '--output_path', type=str, default=None,
                        help=('Путь до выходного изображения. Стандартное значение: '
                              '<путь до файла>_pixel.<расширение файла>.'))
    parser.add_argument('-ps', '--pixel_size', type=int, default=10,
                        help=f'Устанавливает размер пикселя. Стандартное значение: {STANDARD_PIXEL_SIZE}.')
    parser.add_argument('-gs', '--grayscale', type=int, default=50,
                        help=f'Устанавливает градацию серого. Стандартное значение: {STANDARD_GRAYSCALE}.')
    args = parser.parse_args()
    convert(args.input_path, args.output_path, args.pixel_size, args.grayscale)


if __name__ == "__main__":
    main()
