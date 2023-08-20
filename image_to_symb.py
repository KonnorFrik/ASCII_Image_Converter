import numpy as np
from PIL import Image
from typing import Iterable
from arg_parser import *

symb_map = {
    "  ": range(0, 6),
    "` ": range(6, 12),
    "_ ": range(12, 18),
    "- ": range(18, 24),
    ". ": range(24, 30),
    "' ": range(30, 36),
    ", ": range(36, 42),
    ": ": range(42, 48),
    "; ": range(48, 54),
    "\" ": range(54, 60),
    "~ ": range(60, 66),
    "^ ": range(66, 72),
    "* ": range(72, 78),
    "+ ": range(78, 84),
    "! ": range(84, 90),
    "| ": range(90, 96),
    "/ ": range(96, 102),
    "( ": range(102, 108),
    "[ ": range(108, 114),
    "{ ": range(114, 120),
    "? ": range(120, 126),
    "f ": range(126, 132),
    "s ": range(132, 138),
    "h ": range(138, 144),
    "k ": range(144, 150),
    "p ": range(150, 156),
    "w ": range(156, 162),
    "% ": range(162, 168),
    "& ": range(168, 174),
    "$ ": range(174, 180),
    "# ": range(180, 186),
    "@ ": range(186, 192),
    "9 ": range(192, 198),
    "8 ": range(198, 204),
    "0 ": range(204, 210),
    "G ": range(210, 216),
    "B ": range(216, 256),
}

symb_map_reversed = {
    "  ": range(216, 256),
    "` ": range(210, 216),
    "_ ": range(204, 210),
    "- ": range(198, 204),
    ". ": range(192, 198),
    "' ": range(186, 192),
    ", ": range(180, 186),
    ": ": range(174, 180),
    "; ": range(168, 174),
    "\" ": range(162, 168),
    "~ ": range(156, 162),
    "^ ": range(150, 156),
    "* ": range(144, 150),
    "+ ": range(138, 144),
    "! ": range(132, 138),
    "| ": range(126, 132),
    "/ ": range(120, 126),
    "( ": range(114, 120),
    "[ ": range(108, 114),
    "{ ": range(102, 108),
    "? ": range(96, 102),
    "f ": range(90, 96),
    "s ": range(84, 90),
    "h ": range(78, 84),
    "k ": range(72, 78),
    "p ": range(66, 72),
    "w ": range(60, 66),
    "% ": range(54, 60),
    "& ": range(48, 54),
    "$ ": range(42, 48),
    "# ": range(36, 42),
    "@ ": range(30, 36),
    "9 ": range(24, 30),
    "8 ": range(18, 24),
    "0 ": range(12, 18),
    "G ": range(6, 12),
    "B ": range(0, 6),
}

def load_bw_pixels(filename: str) -> np.array or None:
    pixels = None
    with Image.open(filename, formats=("JPEG","PNG")).convert("L") as image:
        pixels = np.asarray(image).astype(int)

    return pixels


def resize(src: np.array, x: int, y: int) -> np.array:
    dst = np.zeros((y, x))
    for y_ind in range(y):
        for x_ind in range(x):
            dst[y_ind, x_ind] = src[y_ind, x_ind]

    return dst


def img_to_symb_block(pixels: Iterable, symb_mapping: dict, block_size: int = 1) -> tuple[str]:
    result_symb_image = list()
    x = 0
    y = 0
    new_size_x = int(len(pixels[0]) / block_size) + 1
    new_size_y = int(len(pixels) / block_size) + 1
    res = np.zeros((new_size_y, new_size_x), dtype=int)

    for col in range(0, len(pixels), block_size):
        x = 0
        for row in range(0, len(pixels[0]), block_size):
            avr = np.average(pixels[col:col+block_size, row:row+block_size])
            res[y, x] = avr
            x += 1
        y += 1

    if x != new_size_x or y != new_size_y:
        res = resize(res, x, y)

    return convert_to_symbls(symb_mapping, res)


def convert_to_symbls(map_table: dict, pixels: np.array) -> tuple[str]:
    result = list()
    for row in pixels:
        for pix in row:
            for symb, rng in map_table.items():
                if pix in rng:
                    result.append(symb)
                    break

    return tuple(result)


def draw(size_x: int, symb_image: list[str]):
    count = 0
    for symb in symb_image:
        if count >= size_x:
            print()
            count = 0

        print(symb, end="")
        count += 1

    print()


def save_image(size_x: int, symb_image: dict, out_file: str):
    with open(out_file, "w") as file:
        count = 0
        for symb in symb_image:
            if count >= size_x:
                file.write("\n")
                count = 0
            file.write(symb)
            count += 1


def main(filename: str, block: int, out_file: str, symb_mapping: dict = symb_map):
    pixels = load_bw_pixels(filename)

    if pixels is None:
        print("[ERROR] Image not loaded")
        return

    size_x = int(len(pixels[0]) / block)
    size_y = int(len(pixels) / block)

    symb_image = img_to_symb_block(pixels, block_size=block, symb_mapping=symb_mapping)

    if not out_file:
        draw(size_x, symb_image)

    else:
        save_image(size_x, symb_image, out_file)


if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename
    block_size = args.block_size
    symbol_table = symb_map_reversed if args.reverse else symb_map
    output_file = args.output

    if block_size < 1:
        print(f"Wrong block size: {block_size}.\nSee usage with '-h' or '--help' option")
        exit(1)

    main(filename, block_size, symb_mapping=symbol_table, out_file=output_file)

