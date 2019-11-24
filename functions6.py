# Dennis Dayan, Watson, 3B, functions6
# VOLUME OF A CYLINDER
# volume = area of base x height
# area = pi x  r-squared (pi multiplied by r-squared)

areaCylinder = 0
Height = 0
volume = 0
radius = 0



def AreaCheckCylinder(radius):
    global areaCylinder
    areaCylinder = 3.14*(radius**2)
    return(areaCylinder)

print("Area of Cylinder is",AreaCheckCylinder(15))


def HeightCheckCylinder(radius, volume):
    global Height
    Height = volume/(3.14* (radius**2))
    return(Height)

print("Height of Cylinder is", HeightCheckCylinder(30, 45))


def cylVolume(r, h):
    global areaCylinder
    global Height
    global volume
    area = 3.14*(r**2)
    Height = h
    volume = area * Height
    return volume

print("Volume of Cylinder is", cylVolume(3, 5))

def cylVol(a, h):
    global volume
    global Height
    Height = h
    volume = a * h
    return volume

print(cylVol(AreaCheckCylinder(3), 5 ) )
