class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.partial_match_table = [0] * len(pattern)
        prefix_len = 0
        for i in range(1, len(pattern)):
            while prefix_len > 0 and pattern[i] != pattern[prefix_len]:
                prefix_len = self.partial_match_table[prefix_len-1]
            if pattern[i] == pattern[prefix_len]:
                prefix_len = prefix_len + 1
                self.partial_match_table[i] = prefix_len

    def find_matches(self, searched_list):
        matches = []
        i_pattern = 0
        for i_list in range(len(searched_list)):
            while i_pattern > 0 and searched_list[i_list] != self.pattern[i_pattern]:
                i_pattern = self.partial_match_table[i_pattern-1]
            if searched_list[i_list] == self.pattern[i_pattern]:
                if i_pattern == len(self.pattern) - 1:
                    matches.append(i_list-i_pattern)
                    i_pattern = self.partial_match_table[i_pattern]
                else:
                    i_pattern = i_pattern + 1
        return matches
