# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from collections import defaultdict

from ...base import StrSplitSolution, answer


def count_points(s: str) -> int:
    count = 0
    winners, nums = s[s.index(":") + 1 :].split(" | ")

    for num in winners.split():
        if num in nums.split():
            count += 1

    if count == 0:
        return 0
    return 2 ** (count - 1)


def count_winning_numbers(s: str) -> int:
    count = 0
    winners, nums = s[s.index(":") + 1 :].split(" | ")

    for num in winners.split():
        if num in nums.split():
            count += 1
    return count


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(32609)
    def part_1(self) -> int:
        return sum(count_points(line) for line in self.input)

    @answer(14624680)
    def part_2(self) -> int:
        cards: defaultdict[int, int] = defaultdict(lambda: 0)

        for idx, line in enumerate(self.input):
            card_id = idx + 1

            cards[card_id] += 1
            num_copies = count_winning_numbers(line)
            if num_copies != 0:
                for c in range(card_id + 1, card_id + 1 + num_copies):
                    cards[c] += cards[card_id]

        return sum(cards.values())
