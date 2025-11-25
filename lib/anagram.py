class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)

        for candidate in word_list:
            cand_lower = candidate.lower()

            # ignore identical word
            if cand_lower == self.word:
                continue

            if sorted(cand_lower) == sorted_word:
                matches.append(candidate)

        return matches
