/*
GE 120
Jewel Lois Cuervo
2023-06864

Exercise 5
*/

// Create function for Latitude.
function getLatitude(distance, azimuth){
    /*
    Compute for the latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float
    */

    if (azimuth % 180 == 90) {return 0} else {
    return (-distance * Math.cos(azimuth * Math.PI / 180.0))}
}

// Create function for Departure.
function getDeparture(distance, azimuth){
    /*
    Compute for the departure of a given line.

    Input:
    distance - float 
    azimuth - float

    Output:
    departure - float
    */

    if (azimuth % 180 == 0) {return 0} else {
    return (-distance * Math.sin(azimuth * Math.PI / 180.0))}     
}

// Create function for converting the azimuth to bearing.
function azimuthToBearing(azimuth){
}

// Create a sentinel loop.
var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.0001],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
]

var lines = []
var sumLat = 0
var sumDep = 0
var sumDist = 0

for (var i = 0; i < data.length; i++){
    // console. log(data [i])

    // define the line, distance, and azimuth for the computation.
    let line = data[i]
    let distance = line[0]
    let azimuth = line [1]

    // Use the function that we created above to solve for the bearing, latitude, and departure of each line.
    let bearing = azimuthToBearing(azimuth)
    let lat = getLatitude(distance, azimuth)
    let dep = getDeparture(distance, azimuth)

    sumLat += lat
    // same as sumlat = sumlat + lat
    sumDep += dep
    sumDist += float(distance)

    lines. push([(i+1), distance, bearing, lat, dep])
}

// If the loop has ended, create a table of summary that shows everything that was inputted.
// console. log(lines)
// console. log("\n\n*)
console.log("LINE NO.".padEnd(10), "DISTANCE".padEnd(10), "BEARING".padEnd(15), "LATITUDE".padEnd(10), "DEPARTURE".padEnd(10))
for (var line of lines){
    console.log(
        line[0].toString().padEnd(10), 
        line[1].toString().padEnd(10), 
        line[2].padEnd (15), 
        Line[3].toPrecision(5).toString().padEnd(10), 
        line[4].toPrecision(5).toString().padEnd(10)
    )
}

// Include the total latitude, departure, and distance in the table.
console. log("SUMMATION OF LAT:", sumLat. toPrecision(5)) 
console. log("SUMMATION OF DEP:", sumDep. toPrecision(5)) 
console. log("SUMMATION OF DIST:", sumDist. toPrecision(5)) 

// Compute for the linear error of closure. 
lec = Math.sqrt (sumLat**2 + sumDep**2) 

// Compute for the relative error of closure.
console. log("LEC:", lec.toPrecision(5))
rec = sumDist/lec
console.log("1: ", Math.floor (rec/1000)*1000)
