class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def __eq__(self, other):
        return(self.x == other.x and self.y == other.y)

    