# File Author: Timothee Guicherd - BCIT Instructor ACIT2515

import csv
import random
import re
import toml 
from pathlib import Path

config = toml.load('config.toml')

LEVEL_FOLDER = "levels"


def generate_levels():
    """Generates 5 levels and saves them to CSV files"""
    # Chance this to be 1 to whatever for how many levels you want. 
    for i in range(1, 10):
        generate_level(i)


def generate_level(level_index, num_pipes=10, start=config['numeric_values']['WIDTH'], width_range=(50, 200), height_range=(50, 400), min_gap=350, max_gap=1000, can_be_inverted=True):
    """
    Generates a level and saves it into a CSV file.
    The CSV format is:
    position,width,height,inverted (for a single pipe)
    """
    position = start
    filepath = Path(LEVEL_FOLDER) / f"level{level_index}.csv"

    with open(filepath, "w", newline="") as fp:
        writer = csv.writer(fp)
        for _ in range(num_pipes):
            width = random.randint(*width_range)
            height = random.randint(*height_range)
            inverted = 0
            if can_be_inverted:
                inverted = 1 if random.random() > 0.5 else 0
            writer.writerow([position, width, height, inverted])
            position += random.randint(min_gap, max_gap)


def load_levels():
    """Loads the CSV files called levelXXX.csv in the levels folder"""
    folder = Path(LEVEL_FOLDER)

    if not folder.exists():
        raise RuntimeError("Cannot load levels.")

    # We start with a dictionary
    levels = {}

    for item in folder.iterdir():
        if item.is_file() and item.suffix == ".csv":
            # If the file name matches the pattern, process it
            matches = re.match(r"level(\d+)\.csv", item.name)
            if not matches:
                continue
            with open(item, "r") as f:
                reader = csv.reader(f)
                data = list(reader)
                if data:
                    # Store the data in the dictionary. Use the level "index" from the filename to store the value.
                    # The CSV files may not be read in sorted order, so we will sort these later
                    levels[int(matches[1])] = data
    if not levels:
        raise RuntimeError("No levels found.")

    # Return the levels sorted by their index
    # return_file[file#][pipe][pipe attribute]
    return [levels[idx] for idx in sorted(levels.keys())]


if __name__ == "__main__":
    if input("Generate levels? Type YES\n") == "YES":
        # generate_levels()
        # print(load_levels()[0])
        # each list among the 10 I am looking at represents the data for one pipe 
        # [position, width, height, inverted]
        print(load_levels())
        
