print("Automated Computations for Vertical Control Survey")
print("Jewel Lois Cuervo")
print("This program computes for the theoretical elevation of BM1 and determines the Geodetic Control Order of the levelling survey using raw data.")

levelling_table = []
total_distance = float()
tp_counter = 1

def floatInput (prompt) :
        while True:
                try:
                        user_input = float(input(prompt))
                        return user_input
                except ValueError:
                        print("Invalid number")

elevation_input = floatInput("Initial Elevation of BM1:")
theoretical_elevation = elevation_input

while True:
    print("Station no.", tp_counter)
    backsight = floatInput("Backsight(m): ")
    foresight = floatInput("Foresight(m): ")
    distance_tp = floatInput("Distance between turning points: ")

    HI = (elevation_input + backsight)
    Elevation = (HI - foresight)
    total_distance = (distance_tp * 2)

    tuple = {backsight, HI, foresight, Elevation}
    levelling_table.append(tuple)

    yn = input("Create new measurement?")
    if yn.lower() == "yes" or yn.lower() == "y":
        tp_counter += 1
        continue
    else:
        break
    
print("\n\n TABLE OF SUMMARY")
print(levelling_table[0][0])
print('{: ^15}{: ^15}{: ^15}{: ^15}{: ^15}'.format("Sta.", "B.S.", "H.I", "F.S.","Elev." ))
for tuple in levelling_table:
      print('{: ^15}{: ^15}{: ^15}{: ^15}{: ^15}'.format(levelling_table[0][0], levelling_table[0][1], levelling_table[0][2],levelling_table[0][3]))












    

    
