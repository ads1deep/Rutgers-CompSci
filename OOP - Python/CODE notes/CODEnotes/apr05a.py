class AlphLetters:
    def __init__(self, startletter, stopletter):
        self.startlet = startletter
        self.stoplet = stopletter
        self.currentlet = startletter
    def __iter__(self):
        return self
    def __next__(self):
        if self.currentlet > self.stoplet:
            raise StopIteration
        answer = self.currentlet
        self.currentlet = chr(ord(self.currentlet) + 1)
        return answer
    
    def __getitem__(self, idx):
        if idx < 0 or idx > ord(self.stoplet) - ord(self.startlet):
            raise IndexError
        return chr(ord(self.startlet) + idx)
    
    

