import json
import yaml
import csv
from dotmap import DotMap
import os
from pathlib import Path


# ***************************************************************** #
# YAML
# ***************************************************************** #
def read_YAML(path: str, b_DotMap: bool = False):
    with open(path) as stream:
        try:
            r_file = yaml.safe_load(stream)
            if b_DotMap:
                return DotMap(r_file)
            else:
                return r_file
        except yaml.YAMLError as exc:
            print(exc)
            return {}


def write_YAML(o_path: str, values):
    if type(values) is dict:
        with open(o_path, 'w') as file:
            yaml.dump(values, file)
    elif type(values) is DotMap:
        with open(o_path, 'w') as file:
            yaml.dump(values.toDict(), file)


# ***************************************************************** #
# JSON
# ***************************************************************** #
def read_JSON(path: str, b_DotMap: bool = False):
    with open(path) as stream:
        try:
            r_file = json.load(stream)
            if b_DotMap:
                return DotMap(r_file)
            else:
                return r_file
        except json.JSONDecodeError as exc:
            print(exc)
            return {}


def write_JSON(o_path: str, values):
    if type(values) is dict:
        with open(o_path, 'w') as file:
            json.dump(values, file)
    elif type(values) is DotMap:
        with open(o_path, 'w') as file:
            json.dump(values.toDict(), file)


# ***************************************************************** #
# CSV
# ***************************************************************** #
def read_CSV(path: str, b_DotMap: bool = False):
    with open(path, mode='r', encoding='utf-8') as stream:
        try:
            r_file = list(csv.DictReader(stream))
            if b_DotMap:
                return DotMap({"data": r_file})
            else:
                return r_file
        except Exception as exc:
            print(exc)
            return []


def write_CSV(o_path: str, values):
    # Convert DotMap to dictionary if necessary
    if type(values) is DotMap:
        data = values.toDict()
    else:
        data = values

    # Extract the list of records from the data
    if type(values) is dict and "data" in data:
        records = data["data"]
    elif type(data) is dict:
        records = list(data.values())
    else:
        records = data

    if not records or not type(records) is list:
        return

    # Write to CSV using DictWriter
    keys = records[0].keys() if type(records[0]) is dict else []
    with open(o_path, 'w', encoding='UTF8', newline='') as f:
        if keys:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(records)
        else:
            writer = csv.writer(f)
            writer.writerows(records)


# ***************************************************************** #
# Path Edit
# ***************************************************************** #
def normpath(path: str):
    if path:
        return os.path.normpath(path)


def home():
    return Path.home()


def desktop():
    return normpath(f"{home()}/Desktop")


def downloads():
    return normpath(f"{home()}/Downloads")


def documents():
    return normpath(f"{home()}/Documents")


def pictures():
    return normpath(f"{home()}/Pictures")


def music():
    return normpath(f"{home()}/Music")


def videos():
    return normpath(f"{home()}/Videos")


def p_root():
    return normpath(f"{os.path.abspath(__file__)}/../../../../")


def parent(path: str, b_Dir=False):
    if path and Path(path).is_file():
        return normpath(f"{path}/../")
    if path and b_Dir:
        return normpath(f"{path}/../")
    return normpath(path)


def basename(path: str, b_Suffix=True):
    if path:
        fp = os.path.basename(path)
        if not b_Suffix:
            return fp.split(".")[0]
        return fp


def suffix(path: str):
    if path:
        breakPath = os.path.basename(path).split(".")[1:]
        tempSuffix = ""
        for __s__ in breakPath:
            tempSuffix += f".{__s__}"
        return tempSuffix


if __name__ == "__main__":
    print(home())
    print(desktop())
    print(downloads())
    print(documents())
    print(pictures())
    print(music())
    print(videos())
    print(p_root())
    print(parent(__file__))
    print(parent(parent(__file__), b_Dir=True))
    print(basename(__file__, False))
    print(suffix("path/AwesomeFile.SAFE.zip"))

