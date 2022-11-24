from pathlib import Path
import os

folder = Path(__file__).parent / "images"


def rm_spaces_rec(folder: Path):
    for file in folder.iterdir():
        if file.is_file():
            file = file.replace(file.with_name(file.name.replace(" ", "_")))
        else:
            file = file.replace(file.with_name(file.name.replace(" ", "_")))
            rm_spaces_rec(file)


def rm_spaces():
    print(folder)
    rm_spaces_rec(folder)


if __name__ == "__main__":
    rm_spaces()
