import turtle
import math

def poligon(t, n, length):
    angle = 360 / n
    poliline(t, n, length, angle)

def circle(t, r):
    c = 2 * math.pi * r
    n = int(c / 3) + 1 # количество углов в многоугольнике
    length = c / n
    poligon(t, n, length)

def poliline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)



# bob = turtle.Turtle()
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.circle(50, 270, 27)


# for x in range(18):
#     bob.fd(200)
#     bob.lt(170)


# poliline(bob, 30, 10, 2)
# circle(bob, 150)
# poligon(bob, 8, 100)

# turtle.mainloop()
# bob.lt(80)
# bob.fd(100)

array = [-88, 5, 7, -1, 3, 0, 11, 2, 5]
def quickSort(array):
    n = len(array)
    l = []
    m = []
    r = []
    if n >= 1:
        for item in array:
            if item > array[0]:
                r.append(item)
            elif item < array[0]:
                l.append(item)
            else:
                m.append(item)
        l = quickSort(l)
        r = quickSort(r)
    else:
        return []
    return l + m + r

print(quickSort(array))