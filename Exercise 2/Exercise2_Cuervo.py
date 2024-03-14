"""
GE 120
Jewel Lois Cuervo
2023-06864

Exercise 2
"""

# Create a counter for the number of lines that the user will input and a tuple for the technical descriptions of the lines. Leave the bracket empty for now.
counter = 1
lines = []

while True:
    print ()
    print("LINE NO.", counter)

# Create an input for the distances and azimuths of the lines
    distance = input("Distance(m): ")
    azimuth = input("Azimuth from the south: ")

# Use If-Else, in case the azimuth entered is in dms or is greater than 360. If so, get the remainder using %.
    if "-" in azimuth: 
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) +(float(seconds)/3600))%360
    else: 
        azimuth = float(azimuth)%360

# Use elif to get the bearing of each line using whatever azimuth is given. The equation in getting the bearing will depend on what condition the azimuth will fall in. 
    if azimuth>0 and azimuth <90: 
        # Since we are looking for the bearing in dms, use the code in the Exercise 1 to convert it from dd. Do this for all the intervals.
        bearing_dd = (azimuth) 
        degrees = int (bearing_dd // 1)
        minutes = (bearing_dd-degrees) * 60
        minutes_whole = int (minutes)
        seconds = (round((minutes - minutes_whole) * 60))
        bearing_dms = (str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds))
        bearing = 'S {: ^10} w'.format(bearing_dms)
    elif azimuth > 90 and azimuth < 180:
        bearing_dd = (180 - azimuth)
        degrees = int (bearing_dd // 1)
        minutes = (bearing_dd-degrees) * 60
        minutes_whole = int (minutes)
        seconds = (round((minutes - minutes_whole) * 60))
        bearing_dms = (str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds))
        bearing ='N {: ^10} W'.format(bearing_dms)
    elif azimuth > 180 and azimuth < 270:
        bearing_dd = (azimuth-180)
        degrees = int (bearing_dd // 1)
        minutes = (bearing_dd-degrees) * 60
        minutes_whole = int (minutes)
        seconds = (round((minutes - minutes_whole) * 60))
        bearing_dms = (str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds))
        bearing = 'N {: ^10} E'.format(bearing_dms)
    elif azimuth > 270 and azimuth < 360:
        bearing_dd = (360 - azimuth)
        degrees = int (bearing_dd // 1)
        minutes = (bearing_dd-degrees) * 60
        minutes_whole = int (minutes)
        seconds = (round((minutes - minutes_whole) * 60))
        bearing_dms = (str(degrees) + "-" + str(minutes_whole) + "-" + str(seconds))
        bearing = 'S {: ^10} E'.format(bearing_dms)
    # There's a posibility that the bearing is along the x or y axis so you also need to include their directions in this elif.
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    # If the azimuth doesn't satisfy any of the conditions above, set bearing as not applicable.
    else:
        bearing = "NOT APPLICABLE"

# Now that we have completed all the needed info, use the code append to put the counter and other technical descriptions in the tuple that we left empty.
    line = [counter, distance, bearing]
    lines.append(line)

# Create a while loop using if else to add a new line. This loop will continue unless said so by typing anything other than yes or y.
    yn = input("Add new line?")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter += 1
        continue
    else:
        break
    
# If the loop has ended, create a table of summary that shows everything that was inputted.
print("\n\n TABLE OF SUMMARY")
# Note: you can adjust the numbers inside the curly bracket based on how far or near you want them to be from one another.
print('{: ^15}{: ^15}{: ^20}'.format("LINE NO.", "DISTANCE(m)", "BEARING"))
for line in lines:
    print('{: ^15}{: ^15}{: ^20}'.format(line[0], line[1], line[2]))

# Print END to show that the code is done.
print("-----END-----")

