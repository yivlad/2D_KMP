def to_file(filename, matches_ij):
    with open(filename, "w") as file:
        file.write(f"{len(matches_ij)}\n")
        file.writelines([f"{i} {j}\n" for (i, j) in matches_ij])
