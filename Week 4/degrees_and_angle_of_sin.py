# The program prompts the user to input angles in degrees, 
# then converts degrees to radians and calculates the sine of the angle, 
# then prints them out

from math import sin, radians

degrees = int(input('Enter an angle in degrees >'))
convertion = radians(degrees)
angle = sin(convertion)
print('The sin of ' + str(degrees) + ' degrees is ' + str(angle))