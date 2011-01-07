class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return '%d/%d/%d' % (self.month, self.day, self.year)

    def print_date_european(self):
        print '%d/%d/%d' % (self.day, self.month, self.year)

    def days_since_2000(self):
        days = (self.year - 2000) * 365
        days += roll[self.month-1]
        days += self.day - 1
        return days


names = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
'Sep', 'Oct', 'Nov', 'Dec' ]

short = ['Sep', 'Apr', 'Jun', 'Nov']

months = {}
for name in names:
    if name == 'Feb':
        months[name] = 28
    elif name in short:
        months[name] = 30
    else:
        months[name] = 31

lengths = [length for (name, length) in months.items()]

def cumulative_sum(t):
    u = []
    total = 0
    for x in t:
        total += x
        u.append(total)
    return u

roll = [0] + cumulative_sum(lengths)

today = Date(6, 12, 2004)
print today
print today.days_since_2000()

