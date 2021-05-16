import argparse
import random
from os import path, mkdir
from random import randint
from sys import stderr


def main():
    args = parse_args()

    for i in range(1, args.file_count + 1):
        file_path = path.join(args.results_directory, f"input{i}.txt")
        with open(file_path, "w") as file:
            search, pattern = create_matrices(args.search_matrix_height, args.search_matrix_width,
                                              args.pattern_matrix_height, args.pattern_matrix_height,
                                              args.maxvalue, args.appearances)
            file_contents = to_file(search, pattern)
            file.write(file_contents)


def parse_args():
    parser = argparse.ArgumentParser(description="Input file generator for 2D pattern finding program")
    parser.add_argument("file_count", metavar="CNT", type=int, help="Number of input files to generate")
    parser.add_argument("results_directory", metavar="OUT", type=str, help="Directory where generated files will be "
                                                                           "placed, will be created if not present")
    parser.add_argument("search_matrix_height", metavar="M", type=int,
                        help="Height of search matrix in generated files")
    parser.add_argument("search_matrix_width", metavar="N", type=int, help="Width of search matrix in generated files")
    parser.add_argument("pattern_matrix_height", metavar="A", type=int,
                        help="Height of pattern matrix in generated files")
    parser.add_argument("pattern_matrix_width", metavar="B", type=int,
                        help="Width of pattern matrix in generated files")
    parser.add_argument("--maxvalue", type=int, dest="maxvalue",
                        help="Maximum value of an element (default=10)", default=10)
    parser.add_argument("--appearances", type=int, dest="appearances",
                        help="Attempted number of appearances of pattern in search matrix (default=5)", default=5)
    parser.add_argument("--overlap", action="store_true", dest="overlap",
                        help="If present overlapping appearances of pattern in search matrix will be attempted")
    args = parser.parse_args()
    if args.search_matrix_width < args.pattern_matrix_width or args.search_matrix_width < args.pattern_matrix_width:
        print(f"Invalid args, search matrix too small", file=stderr)
        exit(-1)
    if not path.exists(args.results_directory):
        mkdir(args.results_directory)
    if not path.isdir(args.results_directory):
        print(f"Failed to create or open directory {args.results_directory}", file=stderr)
        exit(-1)
    return args


def to_file(search, pattern):
    search_str = mat_to_str(search)
    pattern_str = mat_to_str(pattern)
    return f"{len(search)} {len(search[0])} {len(pattern)} {len(pattern[0])}\n{search_str}\n{pattern_str}"


def mat_to_str(mat):
    return "\n".join([" ".join([str(el) for el in row]) for row in mat])


def create_matrices(search_h, search_w, pattern_h, pattern_w, max_el, appearances):
    search = [[randint(0, max_el) for _ in range(search_w)] for _ in range(search_h)]
    pattern = [[randint(0, max_el) for _ in range(pattern_w)] for _ in range(pattern_h)]
    overlap_chance = 1 / appearances
    i = 0
    while i < appearances:
        overlap = random.random() <= overlap_chance
        if overlap:
            i = i + 1
            max_overlap_w = pattern_w//2
            max_overlap_h = pattern_h//2
            min_overlap_w = max(1, pattern_w*2-search_w)
            min_overlap_h = max(1, pattern_h*2-search_h)
            if min_overlap_w > max_overlap_w or min_overlap_h > max_overlap_h:
                print("Invalid dimensions for overlap", file=stderr)
                exit(-1)
            overlap_w = randint(min_overlap_w, max_overlap_w)
            overlap_h = randint(min_overlap_h, max_overlap_h)
            overlap_x0 = pattern_w - overlap_w
            overlap_y0 = pattern_h - overlap_h
            for y in range(overlap_y0, pattern_h):
                pattern[y][overlap_x0:pattern_w] = pattern[y-overlap_y0][0:overlap_w]
            y_0 = randint(0, search_h - pattern_h - overlap_y0)
            x_0 = randint(0, search_w - pattern_w - overlap_x0)
            y_1 = y_0+overlap_y0
            x_1 = x_0+overlap_x0
            for y in range(y_0, y_0 + pattern_h):
                search[y][x_0:(x_0 + pattern_w)] = pattern[y - y_0]
            for y in range(y_1, y_1 + pattern_h):
                search[y][x_1:(x_1 + pattern_w)] = pattern[y - y_1]
        else:
            y_0 = randint(0, search_h - pattern_h)
            x_0 = randint(0, search_w - pattern_w)
            for y in range(y_0, y_0 + pattern_h):
                search[y][x_0:(x_0 + pattern_w)] = pattern[y - y_0]
        i = i + 1
    return search, pattern


if __name__ == "__main__":
    main()
