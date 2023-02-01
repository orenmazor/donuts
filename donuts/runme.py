import argparse
from random import shuffle
from typing import Dict, List

parser = argparse.ArgumentParser(description="Generate donut pairings")
parser.add_argument("-f", help="newline separated file of names", dest="filename")


def names(filename: str) -> List[str]:
    raw = open(filename).read().strip()
    return [name.strip() for name in raw.split()]


def pairup(people: List[str]) -> Dict[str, str]:
    # randomize the list
    shuffle(people)

    # give me pairs of two

    # when python 3.12 drops:
    # pairs = batched(people, 2)

    for i, k in zip(people[0::2], people[1::2]):
        print(f"{i} meet {k}")


if __name__ == "__main__":
    parsed = parser.parse_args()

    pairup(names(parsed.filename))
