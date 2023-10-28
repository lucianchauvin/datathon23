import json

FILENAME = "dataset/aircraft carrier.ndjson"

def get_data(filename):
    with open(filename, "r") as infile:
        for line in infile:
            line = line.rstrip()

            jsonObj = json.loads(line)

            yield jsonObj

if __name__ == "__main__":
    print(next(get_data(FILENAME)))
