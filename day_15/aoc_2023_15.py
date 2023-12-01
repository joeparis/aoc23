#!/usr/bin/env python3


from pathlib import Path

from aocd import data  # https://pypi.org/project/advent-of-code-data/
from dotenv import load_dotenv


def setup() -> None:
    if not Path("input.txt").is_file():
        with Path("input.txt").open(mode="w", encoding="UTF-8") as in_file:
            in_file.write(data)


def solve_part_one() -> None:
    pass


def solve_part_two() -> None:
    pass


if __name__ == "__main__":
    load_dotenv()
    setup()
    solve_part_one()
    # solve_part_two()
