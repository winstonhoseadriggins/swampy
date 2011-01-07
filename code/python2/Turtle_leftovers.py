    def disc(self, radius=1, steps=32):
        self.push()
        self.fan()

        self.vertex()
        self.fd(radius)
        self.vertex()

        dtheta = 360.0/steps
        self.yaw(90 + dtheta / 2)
        circum = 2.0 * math.pi * radius
        for i in range(steps):
            self.fd(circum/steps)
            self.yaw(dtheta)
            self.vertex()

        self.end()
        self.pop()
        

    def polygon(self, radius, steps):
        self.fd(radius)
        t = [self.position()]

        dtheta = 360.0/steps
        self.yaw(90 + dtheta / 2)
        circum = 2.0 * math.pi * radius
        for i in range(steps):
            self.fd(circum/steps)
            self.yaw(dtheta)
            t.append(self.position())
        return t
        
    def shell(self, radius=1, steps=32):

        self.push()

        self.zig(z=radius)
        self.sphere(0.3 * radius)
        self.zag(z=radius)

        height = radius        
        self.zig(y=height)
        t = [self.position()]
        self.zag(y=height)

        self.push()
        self.up(0.6 * height)
        t1 = self.polygon(0.6 * radius, steps)
        self.pop()
        
        self.push()
        t2 = self.polygon(radius, steps)
        self.pop()
        
        self.fan(t+t1)
        self.end()

        t3 = interleave(t2, t1)
        self.strip(t3)
        self.end()

        t = [self.position()]
        t2.reverse()
        self.fan(t+t2)
        self.end()

        self.pop()

def vector_sub(a, b):
    return [x - y for (x, y) in zip(a, b)]

def interleave(t1, t2):
    # precondition: len(t1) is one greater than len(t2)
    res = t1 + t2
    res[0::2] = t1
    res[1::2] = t2
    return res

