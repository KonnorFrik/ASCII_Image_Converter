import numpy as np
from PIL import Image

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

def draw(size_x: int, size_y: int, symb_image: list[str]):
    count = 0
    for symb in symb_image:
        if count >= size_x:
            print()
            count = 0

        print(symb, end="")
        count += 1

    print()


def main(filename: str):
    pixels: np.array = None
    symb_mapping: dict = symb_map
    #symb_mapping: dict = symb_map_reversed

    with Image.open(filename, formats=("JPEG","PNG")).convert("L") as image:
        pixels = np.asarray(image).astype(int)

    if pixels is None:
        print("[ERROR] Image not loaded")
        return

    size_x = len(pixels[0])
    size_y = len(pixels)

    result_symb_image = list()

    for row in pixels:
        for pix in row:
            for symb, rng in symb_mapping.items():
                if pix in rng:
                    result_symb_image.append(symb)
                    break

    draw(size_x, size_y, result_symb_image)


if __name__ == "__main__":
    import sys
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Filename not given")
        exit(1)

    main(filename)
    #draw(x, y, img)
    #print("size:", x, y)
    #print(len(img))
