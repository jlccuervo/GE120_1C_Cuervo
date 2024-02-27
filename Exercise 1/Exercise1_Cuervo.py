"""
GE 120
Exercise 1
Jewel Lois Cuervo
2023-06864
"""

# Convertion of DD to DMS

dd = 118.42069
print("DD:", dd)

# Kunin si degree part: simply use the operation int (x) where x is the dd
degrees = int (dd // 1)
print("Degrees:", degrees)

# Kunin si minutes: subtract degrees to dd then multiply the difference to 60 (1 degree = 60 minutes).
minutes = (dd-degrees) * 60
print("Minutes with decimals not rounded:", minutes)

# Note: the product of the previous operation has a decimal. use the operation int (x) to convert it to integer
minutes_whole = int (minutes)
print("Minutes in whole number:", minutes_whole)

# Kunin si seconds: subtract the minutes in whole number to the minutes with decimal then multiply the difference to 60. (1 minute = 60 seconds)
seconds = (minutes - minutes_whole) * 60
print("Seconds with decimals not rounded:", seconds)

# Note: Round the seconds into 2 decimal places
second_rounded = (round(seconds, 2))
print("Seconds with 2 Decimal:", second_rounded)

# Cnnverted DD to DMS
print("DMS:" + str(degrees) + "-" + str(minutes_whole) + "-" + str(second_rounded))




# Conversion of DMS to DD

dms = "118-25-14.48"

# Note: split the dms string to create a list of values
values = dms.split("-")
print("Values:", values)

# Note: define the DMS values by using the operation int (x) to degrees and minutes and float to seconds to keep its decimals 
degrees = int (values [0])
minutes = int (values [1])
seconds = float (values [2])

# Note: Divide minutes to 60 and seconds to 3600. Add their quotients together with degrees
dd = degrees + (minutes/60) + (seconds/3600)
print("DD with decimals not rounded:", dd)

# Converted DMS to DD
dd_rounded = (round(dd, 6))
print("DD:", dd_rounded)


