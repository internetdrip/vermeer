from PIL import Image

from typing import Generator, Tuple


def extract_scheme(
    path: str, top: int = 30, step: int = 1
) -> Generator[Tuple[int, int, int], None, None]:

    image = Image.open(path).convert("RGB")

    width, height = image.size

    values = [
        image.getpixel((x, y))
        for x in range(width)
        for y in range(height)
    ]

    # Get relevance for each pixel
    values_dict = {value: 0 for value in values}

    for value in values:
        values_dict[value] += 1

    # Sort RGB values by relevance
    values = sorted(
        values_dict.items(),
        key=lambda value: value[1],
        reverse=True,
    )

    yield from map(
        lambda k: k[0],
        (values[i] for i in range(0, top * step, step))
    )
