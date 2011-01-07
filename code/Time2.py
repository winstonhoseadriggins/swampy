class Time:

    def __init__(self, seconds=0):
        # given the number of seconds since midnight, initialize
        # a Time object with attributes hours, minutes and seconds
        self.hours = seconds/3600
        seconds -= self.hours * 3600
        self.minutes = seconds/60
        seconds -= self.minutes * 60
        self.seconds = seconds

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)

    def convert_to_seconds(self):
        # take a Time object and compute the number of seconds
        # since midnight
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

    def add(self, other):
        seconds = self.convert_to_seconds() + other.convert_to_seconds()
        return Time(seconds)

# if a movie starts at noon...
noon_time = Time(12 * 60 * 60)

# and the run time of the movie is 109 minutes...
movie_minutes = 109
run_time = Time(movie_minutes * 60)

# what time does the movie end?
end_time = noon_time.add(run_time)
print end_time
