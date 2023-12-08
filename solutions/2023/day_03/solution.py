# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3
import re
from collections import defaultdict
from operator import mul

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    def padded_input(self) -> list[str]:
        width = len(self.input[0])
        # ensure every line is the same length; we'll mess up lines if it's not
        assert all(len(l) == width for l in self.input)

        return [
            "." * (width + 2),
            *[f".{l}." for l in self.input],
            "." * (width + 2),
        ]

    # @answer(1234)
    def part_1(self) -> int:
        totals = 0
        grid = self.padded_input()
        symbol = re.compile(r"[^\w.]")

        for line_num, line in enumerate(grid):
            for number in re.finditer(r"\d+", line):
                checks = [
                    symbol.search(
                        grid[line_num - 1][number.start() - 1 : number.end() + 1]  # top
                    ),
                    symbol.search(line[number.start() - 1]),  # left
                    symbol.search(line[number.end()]),  # right
                    symbol.search(
                        grid[line_num + 1][
                            number.start() - 1 : number.end() + 1
                        ]  # bottom
                    ),
                ]

                if any(checks):
                    totals += int(number.group())
        return totals

    # @answer(1234)
    def part_2(self) -> int:
        gears: dict[tuple[int, int], list[int]] = defaultdict(list)
        grid = self.padded_input()

        for line_num, line in enumerate(grid):
            for number in re.finditer(r"\d+", line):
                if "*" in (
                    l := grid[line_num - 1][number.start() - 1 : number.end() + 1]
                ):
                    assert l.count("*") == 1
                    gears[(line_num - 1, number.start() - 1 + l.index("*"))].append(
                        int(number.group())
                    )

                if line[number.start() - 1] == "*":
                    gears[(line_num, number.start() - 1)].append(int(number.group()))

                if line[number.end()] == "*":
                    gears[(line_num, number.end())].append(int(number.group()))

                if "*" in (
                    l := grid[line_num + 1][number.start() - 1 : number.end() + 1]
                ):
                    assert l.count("*") == 1
                    gears[(line_num + 1, number.start() - 1 + l.index("*"))].append(
                        int(number.group())
                    )

        return sum([mul(*nums) for nums in gears.values() if len(nums) == 2])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
