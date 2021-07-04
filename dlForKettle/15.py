from datetime import datetime
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
    
    '''
        Перегрузка оператора + слева. Объект должен находиться слеав от +
        obj + 10
    '''
    def __add__(self, value):
        self.x += value
    '''
       Перегрузка оператора + справа. Объект должен находиться справа от +
       10 + obj
    '''
    def __radd__(self, value):
        self.__add__(value)

def point_in_circle(circle, point):
    if abs(point.x - circle.x)**2 + abs(point.y - circle.y)**2 < circle.r**2:
        print('This point is contained in the circle')
    else:
        print('This point isn\'t contained in the circle')

if __name__ == '__main__':
    circle = Circle(150, 100, 75)
    point = Point(177, 226)
    point_2 = Point(150, 100)

    point_2 + 70
    print(point_2.x)
    20 + point_2
    print(point_2.x)
    point_in_circle(circle, point)

class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        # The problem is the default value for contents.
        # Default values get evaluated ONCE, when the function
        # is defined; they don't get evaluated again when the
        # function is called.

        # In this case that means that when __init__ is defined,
        # [] gets evaluated and contents gets a reference to
        # an empty list.

        # After that, every Kangaroo that gets the default
        # value gets a reference to THE SAME list.  If any
        # Kangaroo modifies this shared list, they all see
        # the change.

        # The next version of __init__ shows an idiomatic way
        # to avoid this problem.
        self.name = name
        self.pouch_contents = contents

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        # In this version, the default value is None.  When
        # __init__ runs, it checks the value of contents and,
        # if necessary, creates a new empty list.  That way,
        # every Kangaroo that gets the default value gets a
        # reference to a different list.

        # As a general rule, you should avoid using a mutable
        # object as a default value, unless you really know
        # what you are doing.
        self.name = name

        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)