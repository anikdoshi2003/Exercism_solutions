def equilateral(sides):
    a, b, c = sides

    # Check that all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if all(side > 0 for side in sides) and (a + b > c) and (a + c > b) and (b + c > a):
        return sides[0] == sides[1] == sides[2]
    else:
        return False


def isosceles(sides):
    a, b, c = sides

    # Check that all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if all(side > 0 for side in sides) and (a + b > c) and (a + c > b) and (b + c > a):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    else:
        return False



def scalene(sides):
    a, b, c = sides

    # Check that all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if all(side > 0 for side in sides) and (a + b > c) and (a + c > b) and (b + c > a):
        return sides[0] != sides[1] and sides[1]!= sides[2] and sides[0] != sides[2]
    else:
        return False
