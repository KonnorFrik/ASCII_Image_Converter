from PIL import Image
import numpy as np

def settle(arr) -> np.array:
    return np.where(arr < 255, np.where(arr > 0, arr, 0), 255)


def recolor(t) -> np.array:
    r, g, b = t
    max_r, max_g, max_b = 255, 0, 255  # Фиолетовый
    min_r, min_g, min_b = 0, 0, 0  # Черный
    return settle(min_r + r * (max_r - min_r) / 256), settle(min_g + g * (max_g - min_g) / 256), settle(min_b + b * (max_b - min_b) / 256)


def myhandler_black_n_white(nearby: np.array):
    result = np.zeros(shape=nearby.shape, dtype=nearby.dtype) # int64

    bright_koef = 6
    for x_ind in range(len(nearby)):
        for y_ind in range(len(nearby[x_ind])):
            pixel = nearby[x_ind, y_ind]

            #pixel.fill(pixel.mean().astype(int))
            pixel[:] = pixel.mean().astype(int)

            result += ((nearby - pixel) / bright_koef).astype(int)

    result = settle(result)
    return result


def main(filename: str):
    with Image.open(filename, formats=("JPEG","PNG")) as image:
        #image = image.convert("L")

        #image_processed = Image.new('RGB', (image.size[0], image.size[1] * 2))
        #pixels = image.load()
        pixels: np.array = np.asarray(image).astype(int)

        #pixels_processed = image_processed.load()
        #pixels_processed: np.array = np.asarray(image_processed)
        pixels_processed: np.array = np.zeros(shape=pixels.shape, dtype=pixels.dtype)

        resolution = 3
        for row in range(0, len(pixels[0])):
            for col in range(0, len(pixels[:,0])):
                block = pixels[row:row + resolution, col:col + resolution]
                pixels_processed[row:row + resolution, col:col + resolution] = myhandler_black_n_white(nearby=block)

    Image.fromarray(pixels_processed.astype("uint8")).show()

if __name__ == "__main__":
    import sys
    try:
        file = sys.argv[1]
    except IndexError:
        print("Filename not given")
        exit(1)

    import datetime
    start = datetime.datetime.now()
    main(file)
    print(datetime.datetime.now() - start)

