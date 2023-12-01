#!/usr/bin/env python3


from pathlib import Path

from aocd import data
from dotenv import load_dotenv


def setup() -> None:
    if not Path("input.txt").is_file():
        with Path("input.txt").open(mode="w", encoding="UTF-8") as in_file:
            in_file.write(data)


def part_1():
    pass


def part_2():
    pass


if __name__ == "__main__":
    load_dotenv()
    print(data)
