import math
def polysum(n,s) :
    # function returns sum value of polygon area and square of perimeter of polygon
    # 'n' represents number of sides of polygon
    # 's' represents length of each side.
    # Area of regular polygon =  (0.25*n*s^2)/tan(pi/n)
    # Perimeter of a polygon = n * s
    if (float(n) - int(n) > 0):
        print("Fractional number of side")
        return(None)
    else:
        n = float(n)
        s = float(s)
        area = (0.25 * n * (s**2) )/ math.tan(math.pi/n)
        perimeter_square = (n * s)**2
    return(round(area+ perimeter_square,4))
    
print(polysum(3,2.05))