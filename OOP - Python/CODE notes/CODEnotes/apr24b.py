class Queue:
    def __init__(self):
        self.__qlist = []
    def insert(self, item):
        self.__qlist.append(item)
    def remove(self):
        if not self.empty():
            frnt = self.__qlist[0]
            self.__qlist = self.__qlist[1:]
            return frnt
    def front(self):
        if not self.empty():
            return self.__qlist[0]
    def empty(self):
        return len(self.__qlist) == 0
    def size(self):
        return len(self.__qlist)
