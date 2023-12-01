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
        inputs = in_file.readlines()

    calibration_value_sum = 0
    for line in inputs:
        match = re.findall(r"\d", line)
        if match:
            calibration_value = int(match[0] + match[-1])
            # print(calibration_value)
            calibration_value_sum += calibration_value

    print(calibration_value_sum)


def solve_part_two(file: str) -> None:
    digits: dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    with Path(file).open(mode="r", encoding="utf-8") as infile:
        inputs = infile.readlines()

    calibration_value_sum = 0

    for line in inputs:
        l_digit_index = len(line)
        l_digit = ""

        for value in digits:
            idx = line.find(value)
            if idx < l_digit_index and idx >= 0:
                l_digit_index = idx
                l_digit = value

        r_digit_index = -1
        r_digit = ""

        for value in digits:
            idx = line.rfind(value)
            if idx > r_digit_index and idx >= 0:
                r_digit_index = idx
                r_digit = value

        # print(f"{digits[l_digit]}{digits[r_digit]}")
        calibration_value_sum += int(f"{digits[l_digit]}{digits[r_digit]}")

    print(calibration_value_sum)


if __name__ == "__main__":
    load_dotenv()
    setup()
    # solve_part_one("test_data_01.txt")
    solve_part_one("input.txt")
    # solve_part_two("test_data_02.txt")
    solve_part_two("input.txt")
