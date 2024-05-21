"""
GE 120
Jewel Lois Cuervo
2023-06864

Long Exam 2
"""

#Create a class named parcel and provide the parameter: owner and area
class Parcel:
    def __init__ (self, owner, area):
        self.owner = owner
        self.area = area

    #Create a method for the Parcel object that classifies the lot area to Residential, Private Agricultural, and Public Agricultural
    def getClassification(self):
        if self.area < 10000:
            return "Residential"
        elif self.area >= 10000 and self.area <= 120000:
            return "Private Agricultural"
        else:
            return "Public Agricultural"
    
    #Overload the print function
    def __str__(self):
        return f"A parcel of land owned by {self.owner} with an area of {self.area} square meters"
    
    
#Inherit Parcel and create another class named Riparian. Add the parameter "type"
class Riparian(Parcel):
    def __init__ (self, owner, area, type):
        self.owner = owner
        self.area = area
        self.type = type

    #Create a method for the Riparian object that tells if it is adjacent to river or ocean
    def getAdjoiningWaterbody(self):
        if self.type == 1:
            return "Adjacent to River - can be subject to tilting"
        elif self.type == 2:
            return "Adjacent to Ocean(Littoral) - cannot be subject to tilting"
        else:
            return "Invalid Riparian Parcel"
        
#Run the code and see if it works!
parcel1 = Parcel("Jewel", 15000)
print (parcel1.getClassification())

parcel2 = Riparian("Jewel", 15000, 2)
print (parcel2.getAdjoiningWaterbody())
