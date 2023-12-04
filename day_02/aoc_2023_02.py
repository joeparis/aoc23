#!/usr/bin/env python3


import re
from pathlib import Path

from aocd import data  # https://pypi.org/project/advent-of-code-data/
from dotenv import load_dotenv


def setup() -> None:
    if not Path("input.txt").is_file():
        with Path("input.txt").open(mode="w", encoding="UTF-8") as in_file:
            in_file.write(data)


def solve(file: str) -> None:
    with Path(file).open(mode="r", encoding="UTF-8") as in_file:
        games = in_file.readlines()

    total = 0
    power_total = 0

    bag = {"red": 12, "green": 13, "blue": 14}
    patterns = {color: re.compile(rf"(\d*) (?={color})") for color in bag}

    for game in games:
        results = {color: [int(res) for res in patterns[color].findall(game)] for color in bag}
        if (
            all(map(lambda x: x <= bag["red"], results["red"]))
            and all(map(lambda x: x <= bag["green"], results["green"]))
            and all(map(lambda x: x <= bag["blue"], results["blue"]))
        ):
            total += int(re.search(r"Game (\d*)", game).group(1))

        power_total += max(results["red"]) * max(results["green"]) * max(results["blue"])

    print(f"Sum of IDs: {total}")  # 2528
    print(f"Sum of powers: {power_total}")  #


if __name__ == "__main__":
    load_dotenv()
    setup()
    # solve("test_data_01.txt")
    solve("input.txt")
