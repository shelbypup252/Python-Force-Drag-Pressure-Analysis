import math
from scipy import constants as scp


def magnitudeToXComponentForm(magnitude, degDirection):
    radAngle = float((degDirection / (180 / scp.pi))) #converts from degrees to radians
    radcos = math.cos(radAngle) #finds the cosine of radian-converted degree input

    xcompositepart = magnitude * radcos
    return xcompositepart #returns composite part


def magnitudeToYComponentForm(magnitude, degDirection):
    radAngle = float((degDirection / (180 / scp.pi))) #converts from degrees to radians
    radsin = math.sin(radAngle) #finds the cosine of radian-converted degree input

    ycompositepart = magnitude * radsin
    return ycompositepart #returns composite part


def pressureCalculation(height):
    
    
    if height < 11000:
        temp = float(15.04 - (0.00649 * height))
        pressure = float(101.29 * ( ( (temp + 273.1) / 288.08) ** 5.256) )
    
    
    if (height > 11000 and height < 25000):
        temp = float(-56.46)
        pressure = float(22.65 * (math.exp(1.73 - (0.000157 * height))) )
        
    
    if (height > 25000):
        temp = float(-131.21 + (0.00299 * height))
        pressure = (2.488 * ( ( (temp + 273.1) / 216.6) ** -11.388))
    
    return pressure


def densityPressureCalculation(height):
    
    
    if height < 11000:
        temp = float(15.04 - (0.00649 * height))
        pressure = float(101.29 * ( ( (temp + 273.1) / 288.08) ** 5.256) )
    
    
    if (height > 11000 and height < 25000):
        temp = float(-56.46)
        pressure = float(22.65 * (math.exp(1.73 - (0.000157 * height))) )
        
    
    if (height > 25000):
        temp = float(-131.21 + (0.00299 * height))
        pressure = (2.488 * ( ( (temp + 273.1) / 216.6) ** -11.388))
    
    density = (pressure / (0.2869 * (temp + 273.1) ) )
    return density


def forceDrag(height, dragCoeff, crossArea, veloc):
    
    density = densityPressureCalculation(height)
    
    forceDrag = ( (1/2) * density * (veloc ** 2) * dragCoeff * crossArea)
    return forceDrag


def forceDragDeg(degAngle):
    degAngleDrag = degAngle + 180
    return degAngleDrag


def forceDragVeloComp(height, dragCoeff, crossArea, velocX, velocY):
    density = densityPressureCalculation(height)
    veloc = float(abs(math.sqrt( (velocX ** 2) + (velocY ** 2) ) ) )
    forceDrag = ( (1/2) * density * (veloc ** 2) * dragCoeff * crossArea)
    return forceDrag


def forceDragDegVeloComp(velocX, velocY):
    dragDegRadians = float(math.atan(velocY / velocX))
    tempDragDegs = float(dragDegRadians * (180/math.pi))
    finalDragDeg = tempDragDegs + 180
    return finalDragDeg




height = float(input('Please input current height [m]: '))
crossArea = float(input('Please input the cross area [m^2]: '))
veloc = float(input('Please input velocity magnitude [m/s]: '))
degAngle = float(input('Please input degree angle: '))
dragCoeff = float(0.50)

pressure = pressureCalculation(height)
density = densityPressureCalculation(height)
velocX = magnitudeToXComponentForm(veloc, degAngle)
velocY = magnitudeToYComponentForm(veloc, degAngle)
forceDrag = forceDrag(height, dragCoeff, crossArea, veloc)
forceDragComp = forceDragVeloComp(height, dragCoeff, crossArea, velocX, velocY)
forceDragDegs = forceDragDegVeloComp(velocX, velocY)

print('VelocX =', velocX)
print('VelocY =', velocY)
print('')
print('Pressure =', pressure)
print('Density =', density)
print('Drag =', forceDrag)
print('Drag(comp) =', forceDragComp)
print('Drag Angle =', forceDragDegs)

