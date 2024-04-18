"""
GE 120
Jewel Lois Cuervo
2023-06864

Exercise 3
"""
from math import cos, sin, radians, sqrt

# Create function for Latitude.
def getLatitude(distance, azimuth):
    '''
    Compute for the latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float
    '''

    latitude = -distance * cos(radians(azimuth))

    return latitude

# Create function for Departure.
def getDeparture(distance, azimuth):
    '''
    Compute for the departure of a given line.

    Input:
    distance - float 
    azimuth - float

    Output:
    departure - float
    '''

    departure = -distance * sin(radians(azimuth))

    return departure

# Create function for converting the azimuth to bearing.
def azimuthToBearing(azimuth):
    '''
    Compute for the DMS bearing of a given angle.

    Input:
    azimuth - float

    Output:
    bearing - string
    '''

# Use if-else in case the user inputs azimuth through DMS or DD.
    if "-" in str(azimuth): #if user gives DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else: #if user gives DD
        azimuth = float(azimuth)%360

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: 45} W'. format (round (azimuth, 3))
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^5} W'. format(round(180 - azimuth,3))
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {: 5} E'. format(round(azimuth-180, 3))
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^5} E'.format(round(360 - azimuth,3))
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "N/A"

    return bearing

# Create a counter for the number of lines that the user will input and a tuple for the technical descriptions of the lines. Leave the bracket empty for now.
counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

# CREATE A SENTINEL CONTROLLED LOOP
while True:
    print()
    print("LINE NO.", counter)

    distance = input("Distance(m): ")
    azimuth = input("Azimuth from the south: ")

# Use the function that we created above to solve for the bearing, latitude, and departure of each line.
    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(azimuth=float(azimuth), distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth), distance=float(distance))

    sumLat += lat
    # same as sumlat = sumlat + lat
    sumDep += dep
    sumDist += float(distance)


    line = (counter, distance, bearing, lat, dep) #create tuple of the line
    # Now that we have completed all the needed info, use the code append to put the counter and other technical descriptions in the tuple that we left empty.
    lines.append(line)

# Create a while loop using if else to add a new line. This loop will continue unless said so by typing anything other than yes or y.
    yn = input("Add new line? ")
    if yn. lower() == "yes" or yn. lower () == "y":
        counter = counter + 1
        continue 
    else:
        break

# If the loop has ended, create a table of summary that shows everything that was inputted.
print ("\n\n")
print ("TABLE OF SUMMARY")
print("___________________________________________________________________________")
# Note: you can adjust the numbers inside the curly bracket based on how far or near you want these to be from one another.
print('{: ^15}{: ^15}{: ^15} {: ^15}{: ^15}' .format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in lines:
    print('{: ^15}{: ^15}{: ^15} {: ^15}{: ^15}'.format(line[0], line[1], line[2], round(line[3],3), round(line[4],3)))
print("___________________________________________________________________________")

print("SUMMATION OF LAT:", round(sumLat, 3))
print ("SUMMATION OF DEP:", round(sumDep, 3))
print("SUMMATION OF DIST:", round(sumDist, 3))

lec = sqrt(sumLat**2 + sumDep**2)

print("LEC:", round(lec, 3))
rec = sumDist/lec
print("REC: 1  : ", round (rec, 3))

constCorrLat = -float(sumLat)/sumDist
constCorrDep = -float (sumDep)/sumDist

for line in lines:
    corr_lat = constCorrLat * float(line[1])
    corr_dep = constCorrDep * float(line [1])

    adjlat = line[3] + corr_lat
    adjDep = line[4] + corr_dep

print("\n\n")
# Print END to show that the code is done.
print("---------END---------")