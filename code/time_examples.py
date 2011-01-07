class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
	return int_to_time(seconds)


    def print_time (self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def after(self, other):
        return self.time_to_int() > other.time_to_int()

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

def time_to_int(t):
    minutes = t.hour * 60 + t.minute
    seconds = minutes * 60 + t.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

#print_time(time)

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second =  0

start.print_time()
end = start.increment(1337)
end.print_time()

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
#print_time(done)


start = Time(9, 45)
duration = Time(1, 35)
print start + duration
print start + 1337
