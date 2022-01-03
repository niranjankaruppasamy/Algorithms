"""
Hackerrank problem
"""

def dayOfProgrammer(year):
    const = 215
    if year == 1918:
        const += 15
        date = 256 - const
        return "{}.09.{}".format(date, year)
    if year < 1917 and year % 4 == 0:
        const += 29
    elif year < 1917 and year % 4 != 0:
        const += 28
    elif year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        const += 29
    else:
        const += 28
    date = 256 - const
    return "{}.09.{}".format(date, year)


print(dayOfProgrammer(1716))