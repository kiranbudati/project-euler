import datetime

# dt = '2001-10-18'
# year, month, day = (int(x) for x in dt.split('-'))    
# answer = datetime.date(year, month, day).weekday()

# print answer

print  datetime.datetime.strptime('Jan  1, 1900', '%B %d, %Y').strftime('%A')