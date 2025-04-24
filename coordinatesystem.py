import math
class LinearCoordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    #Distance between two points: A(x1, y1) and B(x2, y2)
    def distance(self, second):
        temp_x = (self.x - second.x) **2
        temp_y = (self.y - second.y) **2
        dist = float(math.sqrt(temp_x + temp_y))
        return dist

    #Equation of straight line of: A(x1, y1) and B(x2, y2)
    def equation(self, second):
        #Handle vertical lines
        if self.x == second.x:
            return f"x = {self.x}"

        #Slope and constant calculation
        slope = (second.y - self.y)/(second.x - self.x)
        constant = self.y - slope * self.x

        #Handle Slope formatting
        if slope == 1:
            slope_str = "x"
        elif slope == -1:
            slope_str = "-x"
        else:
            slope_str = f"{slope}"

        #Handle Constant formatting
        if constant == 0:
            return f"y = {slope_str}"
        elif constant > 0:
            return f"y = {slope_str}x + {constant}"
        else:
            return f"y = {slope_str}x - {-constant}"
