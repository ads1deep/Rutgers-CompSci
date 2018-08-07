class AlphLetters:
    def __init__(self, startletter, stopletter):
        self.startlet = startletter
        self.stoplet = stopletter
    def __iter__(self):
        return AlphLettersIterator(self.startlet, self.stoplet)
    def __getitem__(self, idx):
        if idx < 0 or idx > ord(self.stoplet) - ord(self.startlet):
            raise IndexError
        return chr(ord(self.startlet) + idx)
    
class AlphLettersIterator:
    def __init__(self, st, sp):
        self.startl = st
        self.stopl = sp
        self.currentlet = self.startl
    def __next__(self):
        if self.currentlet > self.stopl:
            raise StopIteration
        answer = self.currentlet
        self.currentlet = chr(ord(self.currentlet) + 1)
        return answer
