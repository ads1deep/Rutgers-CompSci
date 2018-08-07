class IndClass:
    def __getitem__(self, idx):
        if idx > 50:
            raise StopIteration
        return 2*idx


class Container:
    def __init__(self):
        self.__data = [5, 10, 15, 20, 25]
    def __getitem__(self, idx):
        return self.__data[idx]
    def __setitem__(self, idx, value):
        if idx >= 0 and idx <= 4:
            self.__data[idx] = value
        else:
            raise IndexError
    def __str__(self):
        astr = ""
        for e in self.__data:
            astr = astr + "%d "%(e)
        return astr


