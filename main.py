# -*- coding: utf-8 -*-

def rectangle_area(width, height):
    if width >= 0 and height >= 0:
        area = width * height
        status = "Area calculation successful."
    else:
        area = None
        status = "Error: Dimensions must be non-negative."

    return area, status


    print(status)


# Example usage2:
