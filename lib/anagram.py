# your code goes here!
class Anagram:
    def __init__(self, names) -> None:
        self._name = sorted(names)
    def match(self, words):
        word_list = []
        
        for word in words:
            if sorted(word) == self._name:
                word_list.append(word)

        return word_list