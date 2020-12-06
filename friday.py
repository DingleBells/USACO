"""
ID: kanghee2
LANG: PYTHON3
PROG: friday
"""
#NOTES:
#Find a way for every year on the 13th of month you find the day(use %?) it falls on and increase the value in dict by 1
#Step 1. Find the first day of each month
#Step 2. For every month, find the day the 13th falls on and add to dict
#repeat for x number of years
#use the dictionary to write to the file
#leap years
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and (year % 100) % 4 == 0:
        return True
    return False

years = int(open('friday.in', 'r').readline())
out = open('friday.out','w')
_13thDays = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
leap_years = []
numDaysSince = 12
dayslist = [12]
for year in range(1900, 1900+years):
    months = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]
    if leap_year(year) == True:
        months[1]+=1
    for month in months:
        dayslist.append(numDaysSince+month)
        numDaysSince += month

del dayslist[-1]
daykeys = list(_13thDays.keys())
for pos, day in enumerate(dayslist):
    modded = day%7
    _13thDays[daykeys[modded]] += 1
out.write(f"{_13thDays['Saturday']} {_13thDays['Sunday']} {_13thDays['Monday']} {_13thDays['Tuesday']} {_13thDays['Wednesday']} {_13thDays['Thursday']} {_13thDays['Friday']}\n")
