import sys

from rich.console import Console

from vermeer import extract_scheme


if __name__ == "__main__":
    console = Console()

    for value in extract_scheme(sys.argv[1]):
        console.print(
            stringified := "rgb" + str(value).replace(' ', ''),
            style=stringified, highlight=False
        )
