# sequence_iter.py

class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return Iterator(self.sequence)


class Iterator:

    def __init__(self, sequence: Sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sequence):
            item = self.sequence[self.index]
            self.index += 2
            return item
        else:
            raise StopIteration


if __name__ == '__main__':

    seq = Sequence([1, 2, 3, 4])

    for item in seq:
        print(item)

    for item in iter(seq):
        print(item)