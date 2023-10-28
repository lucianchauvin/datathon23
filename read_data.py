import json
from typing import Generator


def get_data(filename: str) -> Generator:
    with open(filename, "r") as infile:
        for line in infile:
            line = line.rstrip()

            jsonObj = json.loads(line)

            yield jsonObj

if __name__ == "__main__":
    FILENAME = "dataset/aircraft carrier.ndjson"
    print(next(get_data(FILENAME)))
