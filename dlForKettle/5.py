import time
import turtle

t = time.time()
countDays = 60*60*24
print(t // countDays)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    print(n)
    draw(t, length, n-1)
    t.rt(2*angle)
    print('-- ', n)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


t = turtle.Turtle()
draw(t, 30, 3)
turtle.mainloop()