"""
GE 120
Jewel Lois Cuervo
2023-06864

Exercise 4
"""

from math import cos, sin, radians, sqrt

# Create a class of line that includes latitude, departure, and bearing.
class Line:
    # Define the attributes using the __init__ function. Note: You must always include self in the parameters of a class function.
    def __init__(self, distance, azimuth):
        self.distance = distance
        self.azimuth = azimuth

    # Create function for Latitude.
    def latitude(self):
        '''
        Compute for the latitude of a given line.

        Input:
        distance - float
        azimuth - float

        Output:
        latitude - float
        '''

        latitude = -float(self.distance) * cos(radians(self.azimuth))

        return latitude
    
    # Create function for Departure.
    def departure(self):
        '''
        Compute for the departure of a given line.

        Input:
        distance - float 
        azimuth - float

        Output:
        departure - float
        '''

        departure = -float(self.distance) * sin(radians(self.azimuth))

        return departure
    
    # Create function for Bearing.
    def bearing(self):
        '''
        Compute for the DMS bearing of a given angle.

        Input:
        azimuth - float

        Output:
        bearing - string
        '''

        if azimuth > 0 and azimuth < 90:
            bearing = 'S {: 45} W'. format (round (azimuth, 3))
        elif azimuth > 90 and azimuth < 180:
            bearing = 'N {: ^5} W'. format(round(180 - azimuth,3))
        elif azimuth > 180 and azimuth < 270:
            bearing = 'N {: 5} E'. format(round(azimuth-180, 3))
        elif azimuth > 270 and azimuth < 360:
            bearing = 'S {: ^5} E'.format(round(360 - azimuth,3))
        else:
            bearing = 'N/A'

        return bearing

# Create another Class in case the inputted azimuth is exactly 90, 180, 270, or 360.
class Cardinal(Line):

    def __init__(self, distance, azimuth):
        super().__init__(distance, azimuth)

    def bearing(self):
        if azimuth == 0:
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
# Get the summation of the latitude, departure, and distance so we can print it in the table of summary.
sumLat = 0
sumDep = 0
sumDist = 0

# CREATE A SENTINEL CONTROLLED LOOP
while True:
    print()
    print("LINE NO.", counter)

    # Ask for inputs.
    distance = input("Distance(m): ")
    azimuth = input("Azimuth from the south: ")

    # Use if-else in case the user inputs azimuth through DMS or DD.
    if "-" in str(azimuth): #if user gives DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else: #if user gives DD
        azimuth = float(azimuth)%360

    # Use if-else to use the class Cardinal that we made above if the inputted azimuth lies due north, south, east, and west. 
    if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    # If not, it will automatically proceed using the class Line.
    else:
        line = Line(distance, azimuth)

    sumLat += line.latitude()
    # same as sumlat = sumlat + lat
    sumDep += line.departure()
    sumDist += float(line.distance)

    # Now that we have completed all the needed info, use the code append to put the counter and other technical descriptions in the tuple that we left empty.
    lines.append((counter, line.distance, line.bearing(), line.latitude(), line.departure()))

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

print("\n\n")
# Print END to show that the code is done.
print("---------END---------")
        
