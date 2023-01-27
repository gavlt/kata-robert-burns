from typing import List
import argparse
import re
from nltk.tokenize import word_tokenize

parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType("r"), help="filepath of the poem")

class EmptyFileError(Exception):
    pass


def parse_file(file) -> str:
    return file.read()


def calculate_ttr(text: str) -> float:
    tokens = word_tokenize(text)
    print(tokens)
    try:
        return len(set(tokens))/len(tokens)
    except ZeroDivisionError as e:
        raise EmptyFileError from e


if __name__ == "__main__":
    args = parser.parse_args()
    text = parse_file(args.file)
    ttr = calculate_ttr(text)
    print(f"Type-Token Ratio of {args.file.name} is {ttr}")
