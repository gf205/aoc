# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

from re import split

from ...base import StrSplitSolution, answer


def game_is_possible(s: str) -> int:
    game_id = s.split(":")[0].split()[-1]

    dict_bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for subset in s.split(": ")[1].split("; "):
        for i in subset.split(", "):
            if dict_bag[i.split()[-1]] - int(i.split()[0]) < 0:
                return 0

    return int(game_id)


def min_cubes(s: str) -> int:
    dict_bag = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for subset in s.split(": ")[1].split("; "):
        for i in subset.split(", "):
            if int(i.split()[0]) > dict_bag[i.split()[-1]]:
                dict_bag[i.split()[-1]] = int(i.split()[0])

    return dict_bag["red"] * dict_bag["green"] * dict_bag["blue"]


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2268)
    def part_1(self) -> int:
        for line in self.input:
            return sum(game_is_possible(line) for line in self.input)

    # @answer(1234)
    def part_2(self) -> int:
        return sum(min_cubes(line) for line in self.input)
