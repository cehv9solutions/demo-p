def rectangle_area(width, height):
    if width >= 0 and height >= 0:
        area = width * height
        status = "Area calculation successful."
    else:
        area = None
        status = "Error: Dimensions must be non-negative."

    return area, status

# Example usage:
width = 5
height = 10
area, status = rectangle_area(width, height)
if area is not None:
    print(f"{status} The area of the rectangle with width {width} and height {height} is {area}")
else:
    print(status)


# Example usage2: