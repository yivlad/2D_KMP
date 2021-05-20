from random import randint, random
from sys import stderr


class InputGenerator:
    def __init__(self, search_matrix_height, search_matrix_width, pattern_matrix_height, pattern_matrix_width,
                 max_value, appearances, overlap):
        self.search_h = search_matrix_height
        self.search_w = search_matrix_width
        self.pattern_h = pattern_matrix_height
        self.pattern_w = pattern_matrix_width
        self.max_value = max_value
        self.appearances = appearances
        self.overlap = overlap

    def create_matrices(self):
        search = [[randint(0, self.max_value) for _ in range(self.search_w)] for _ in range(self.search_h)]
        pattern = [[randint(0, self.max_value) for _ in range(self.pattern_w)] for _ in range(self.pattern_h)]
        overlap_chance = 1 / self.appearances if self.overlap else 0
        i = 0
        while i < self.appearances:
            perform_overlap = random() <= overlap_chance
            if perform_overlap:
                i = i + 1
                max_overlap_w = self.pattern_w // 2
                max_overlap_h = self.pattern_h // 2
                min_overlap_w = max(1, self.pattern_w * 2 - self.search_w)
                min_overlap_h = max(1, self.pattern_h * 2 - self.search_h)
                if min_overlap_w > max_overlap_w or min_overlap_h > max_overlap_h:
                    print("Invalid dimensions for overlap", file=stderr)
                    exit(-1)
                overlap_w = randint(min_overlap_w, max_overlap_w)
                overlap_h = randint(min_overlap_h, max_overlap_h)
                overlap_x0 = self.pattern_w - overlap_w
                overlap_y0 = self.pattern_h - overlap_h
                for y in range(overlap_y0, self.pattern_h):
                    pattern[y][overlap_x0:self.pattern_w] = pattern[y - overlap_y0][0:overlap_w]
                y_0 = randint(0, self.search_h - self.pattern_h - overlap_y0)
                x_0 = randint(0, self.search_w - self.pattern_w - overlap_x0)
                y_1 = y_0+overlap_y0
                x_1 = x_0+overlap_x0
                for y in range(y_0, y_0 + self.pattern_h):
                    search[y][x_0:(x_0 + self.pattern_w)] = pattern[y - y_0]
                for y in range(y_1, y_1 + self.pattern_h):
                    search[y][x_1:(x_1 + self.pattern_w)] = pattern[y - y_1]
            else:
                y_0 = randint(0, self.search_h - self.pattern_h)
                x_0 = randint(0, self.search_w - self.pattern_w)
                for y in range(y_0, y_0 + self.pattern_h):
                    search[y][x_0:(x_0 + self.pattern_w)] = pattern[y - y_0]
            i = i + 1
        return search, pattern
