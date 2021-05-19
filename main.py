import argparse
from baker_bird import BakerBird
from naive import NaiveSearch
from files_io import from_file, to_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Algorithm for finding patterns in 2D")
    parser.add_argument("input_filename", metavar="IN", type=str, help="Input file containing search and pattern matrices")
    parser.add_argument("output_filename", metavar="OUT", type=str, help="Output file containing indices of matches")
    parser.add_argument('--naive', default=False, action='store_true', help="Use naive quadratic time algorithm instead of Baker-Bird algorithm")
    args = parser.parse_args()

    (M, P) = from_file(args.input_filename)

    strategy = None
    if args.naive:
        strategy = NaiveSearch()
    else:
        strategy = BakerBird()
    matches_ij = strategy.find(M, P)

    to_file(args.output_filename, matches_ij)
