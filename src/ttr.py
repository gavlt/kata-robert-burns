from typing import List
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType("r"), help="filepath of the poem")

class EmptyFileError(Exception):
    pass


def parse_file(file) -> List[str]:
    regexp = r"\b\S+\b"
    words = re.findall(regexp, file.read().lower())
    return words


def calculate_ttr(words: List[str]) -> float:
    unique_len = len(set(words))
    try:
        return unique_len/len(words)
    except ZeroDivisionError as e:
        raise EmptyFileError from e


if __name__ == "__main__":
    args = parser.parse_args()
    words = parse_file(args.file)
    ttr = calculate_ttr(words)
    print(f"Type-Token Ratio of {args.file.name} is {ttr}")
