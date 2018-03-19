from datetime import date
from collections import Counter

counter = Counter()

for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        day = date(year, month, 1)
        counter[day.weekday()] += 1

print counter[6]