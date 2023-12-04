#!/usr/bin/env python3


import re
from pathlib import Path

from aocd import data  # https://pypi.org/project/advent-of-code-data/
from dotenv import load_dotenv


def setup() -> None:
    if not Path("input.txt").is_file():
        with Path("input.txt").open(mode="w", encoding="UTF-8") as in_file:
            in_file.write(data)


def solve_part_one(file: str) -> None:
    with Path(file).open(mode="r", encoding="UTF-8") as in_file:
        games = in_file.readlines()

    bag = {"red": 12, "green": 13, "blue": 14}
    total = 0
    possible = True

    for game in games:
        for color in bag:
            pattern = re.compile(rf"(\d*) (?={color})")
            for count in pattern.findall(game):
                if int(count) > bag[color]:
                    possible = False

        if possible:
            total += int(game.split(":")[0].split()[-1])
        possible = True

    print(total)


def solve_part_two(file: str) -> None:
    with Path(file).open(mode="r", encoding="utf-8") as infile:
        inputs = infile.readlines()


if __name__ == "__main__":
    load_dotenv()
    setup()
    # solve_part_one("test_data_01.txt")
    solve_part_one("input.txt")
    # solve_part_two("test_data_02.txt")
    # solve_part_two("input.txt")
