def draw(t, dist, n):
    if n == 0:
        return
    fd(t, dist*n)
    lt(t, 45)
    draw(t, dist, n-1)
    rt(t, 90)
    draw(t, dist, n-1)
    lt(t, 45)
    bk(t, dist*n)

world.clear()
bob = Turtle(world)
bob.delay = 0.01
lt(bob)
draw(bob, 10, 7)
