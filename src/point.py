class Point:
    
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #Methods
    def setAbsis(self,x):
        self.x = x
    def setOrdinat(self,y):
        self.y = y
    def getAbsis(self):
        return self.x
    def getOrdinat(self):
        return self.y
    def printPoint(self):
        print(f"({self.x}, {self.y})")