class Circle:
    ''' 
        class creates circle 
    '''

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

class Point:
    '''
        class creates point
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

def point_in_circle(circle, point):
    if abs(point.x - circle.x)**2 + abs(point.y - circle.y)**2 < circle.r**2:
        print('This point is contained in the circle')
    else:
        print('This point isn\'t contained in the circle')

if __name__ == '__main__':
    circle = Circle(150, 100, 75)
    point = Point(177, 226)
    point = Point(150, 100)
    point_in_circle(circle, point)