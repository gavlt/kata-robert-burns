import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType("r"), help="filepath of the poem")


def parse_file(file):
    pass


def calculate_ttr(text) -> float:
    pass


if __name__ == "__main__":
    args = parser.parse_args()
    text = parse_file(args.file)
    ttr = calculate_ttr(text)
    print(f"Type-Token Ratio of {args.file.name} is {ttr}")
