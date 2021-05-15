import argparse
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
                                              args.max_element_value)
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
    parser.add_argument("max_element_value", metavar="MAX_EL", type=int,
                        help="Maximum value of an element (default=10)", default=10)
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


def create_matrices(search_h, search_w, pattern_h, pattern_w, max_el):
    search = [[randint(0, max_el) for _ in range(search_w)] for _ in range(search_h)]
    pattern = [[randint(0, max_el) for _ in range(pattern_w)] for _ in range(pattern_h)]
    for _ in range(0, 5):
        y_0 = randint(0, search_h - pattern_h)
        x_0 = randint(0, search_w - pattern_w)
        for y in range(y_0, y_0 + pattern_h):
            search[y][x_0:(x_0 + pattern_w)] = pattern[y - y_0]
    return search, pattern


if __name__ == "__main__":
    main()
