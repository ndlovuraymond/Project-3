import re
import numpy as np

# giving the user instructions
print("Please input points in x y representation. \nType END to finish.")

# accepting user inputs
inputting_data = True
points = []
count = 1
while inputting_data:
    try:
        user_points = input(f"P#{count}: ")
        if user_points.upper() == "END":
            break
        else:
            try:
                cur_points = user_points.split()
                x, y = cur_points
                x = float(x)
                y = float(y)
                current_points = [x, y]
                points.append(current_points)
            except:
                print("Please enter valid points e.g. 1 2 where x=1 & y=2")
                continue
    except:
        print("Please enter valid points e.g. 1 2 where x=1 & y=2")
        continue
    count += 1

# displaying the function in the form f(x)
x = [x[0] for x in points]
y = [y[1] for y in points]
function = ""
# finding the values for the function f(x)
values = np.polyfit(x, y, 2)
a, b, c = values
a = round(a, 4)
b = round(b, 5)
c = round(c, 5)
print("Resulting polynomial will be of the order 2")
count = 1
string = "f(x) = "
for item in values:
    if count == 1:
        string += str(a) + "x^2"
    elif count == 2:
        if b >= 0:
            string += " + "
        else:
            b = b * -1
            string += " - "
        string += str(b) + "x^1"
    elif count == 3:
        if c >= 0:
            string += " + "
        else:
            c = c * -1
            string += " - "
        string += str(c)
    count += 1
print(string)
# making the function into the string so that I can use it to get the derivative later
function = string
# display polynomial for -1,0,1
for i in range(-1, 2):
    result = 0
    for j in range(0, 3):
        result = result * i + values[j]
    string = f"f({i}) = " + str(result)
    print(string)

# initialising empty list of derivatives so that collection of derviates for root function is easier
my_derivatives = []
# getting the derivative of the function
def poly_dev(poly, dev):
    c = 0
    string = ""
    for i in range(1, 3):
        poly[i - 1] = (len(poly) - (i + c)) * poly[i - 1]
        my_derivatives.append(poly[i - 1])
        cur_string = str(round(poly[i - 1], 9))
        if i == 1:
            string += cur_string
            string += "x^1"
        else:
            string += cur_string
    c += 1
    return string


# showing the user the derivative
print("Derivative:")
derivative = poly_dev(values, 1)
print("f'(x) =" + str(derivative))

# method for finding the root
def finding_root(x, n):
    def function(x):
        result = 0
        for j in range(0, 3):
            result = result * x + values[j]
        return result

    def derivative_function(x):
        result = 0
        for j in range(0, 2):
            result = result * x + my_derivatives[j]
        return result

    for intercept in range(1, n):
        i = x - (function(x) / derivative_function(x))
        x = i
    print(f"The root was found to be {x}")
    # not working as intended fixes needed


finding_root(x=1, n=len(values))
