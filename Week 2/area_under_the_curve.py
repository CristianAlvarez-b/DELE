def f(x):
    return x ** 2

def area_under_curve(a, b, n):
    dx = (b - a) / n  # Width of each rectangle
    total_area = 0

    for i in range(n):
        x_left = a + i * dx  # Left boundary of the rectangle
        x_right = x_left + dx  # Right boundary of the rectangle
        height = f(x_left)  # Height of the rectangle (using left boundary)
        area = height * dx  # Area of the rectangle
        total_area += area

    return total_area

a = 2  # Lower limit of integration
b = 3  # Upper limit of integration
n = 1000  # Number of rectangles for approximation

result = area_under_curve(a, b, n)
print("Approximate area under the curve:", result)
