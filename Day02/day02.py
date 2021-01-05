from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import List, Union, TextIO


@dataclass
class Password:

    required: str
    first: int
    second: int
    value: str

    @classmethod
    def build_from_data_factory(cls, data: Union[List[str], TextIO]) -> List[Password]:
        passwords = []

        for line in data:
            range, character, value = line.strip().split(" ")
            first, second = [int(x) for x in range.split("-")]
            passwords.append(Password(required=character.strip(":"), first=first, second=second, value=value))

        return passwords

    def is_valid_based_on_character_count(self) -> bool:
        counts = defaultdict(int)

        for character in self.value:
            counts[character] += 1

        return self.first <= counts.get(self.required, -1) <= self.second

    def is_valid_based_on_character_location(self) -> bool:
        num_valid = 1 if self.value[self.first - 1] == self.required else 0
        num_valid += 1 if self.value[self.second - 1] == self.required else 0
        return num_valid == 1


if __name__ == '__main__':
    with open("data.txt", "r") as data:
        passwords = Password.build_from_data_factory(data)

    print(sum([password.is_valid_based_on_character_count() for password in passwords]))
    print(sum([password.is_valid_based_on_character_location() for password in passwords]))
