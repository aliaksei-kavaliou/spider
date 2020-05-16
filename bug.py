#!/usr/bin/env python3

from spider import Spider

def main():
    bug_file = input("Load bug file: ")
    bug = load_file(bug_file)

    if (bug is None):
        exit(1)

    landscape_file = input("Load landscape file: ")
    landscape = load_file(landscape_file)

    if (landscape is None):
        exit(1)
   
    spider = Spider(landscape, bug)
    print("Found", spider.search(), "bugs.")


def load_file(path: str) -> list:
    """load file data to matrix."""
    try :
        with open(path, 'r') as f:
            return [list(line.rstrip("\n")) for line in f.readlines()]
    except IOError:
        print("Could not read file:", path)

    return None 


if __name__ == "__main__":
    main()