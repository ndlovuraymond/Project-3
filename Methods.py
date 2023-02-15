class Polynomial_Calc:
    def __init__(self):
        self.points = []
        self.coefficients = []

    def display_values(self):
        print("Values of the polynomial:")
        for x in [-1, 0, 1]:
            y = 0
            for i in range(len(self.coefficients) - 1, -1, -1):
                y = y * x + self.coefficients[i]
            print(f"f({x}) = {y}")

    def show_values(self):
        print("Please input points in x y representation. \nType END to finish.")
        self.input_points()
        self.display_values()
        self.find_root(0, 1, 1e-6)
        print(f"The root found for x = {self.find_root(0, 1, 1e-6)}")

    def input_points(self):
        self.points = []
        inputting_data = True
        i = 1
        # collecting coordinates
        while inputting_data:
            value = input(f"Enter the x and y coordinates of point {i}: ")
            if len(value.split()) == 2:
                cur_value = value.split()
                x = float(cur_value[0])
                y = float(cur_value[1])
                self.points.append((x, y))
                i += 1
            # ending the collection based on user input
            elif value.upper() == "END":
                inputting_data = False
            else:
                print("Please enter coordinates like this: 2 1 where X is 2 and Y is 1")
        x_axis = [p[0] for p in self.points]
        y_axis = [p[1] for p in self.points]
        n = len(x_axis)
        vandermonde = [[xi**j for j in range(n)] for xi in x_axis]
        coefficients = [0] * n

        i = 0
        while i < n:
            current_pivot = vandermonde[i][i]
            if current_pivot == 0:
                i += 1
                continue
            p = i + 1
            while p < n:
                factor = vandermonde[p][i] / current_pivot
                for k in range(n):
                    vandermonde[p][k] -= factor * vandermonde[i][k]
                y_axis[p] -= factor * y_axis[i]
                p += 1
            i += 1

        count = n - 1
        while count > -1:
            cur_pivot = vandermonde[count][count]
            if cur_pivot == 0:
                coefficients[count] = 0
            else:
                coefficients[count] = y_axis[count] / vandermonde[count][count]
                for j in range(i):
                    y_axis[j] -= vandermonde[j][count] * coefficients[count]
            count += -1

        self.coefficients = coefficients

    def find_root(self, x0, x1, eps):
        f0 = 0
        f1 = 0
        for i in range(len(self.coefficients) - 1, -1, -1):
            f0 = f0 * x0 + self.coefficients[i]
            f1 = f1 * x1 + self.coefficients[i]
        while abs(f1) > eps:
            try:
                x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
                f2 = 0
                for i in range(len(self.coefficients) - 1, -1, -1):
                    f2 = f2 * x2 + self.coefficients[i]
                x1 = x2
                f1 = f2
                root = x1
            # try except block incase zero division
            except ZeroDivisionError:
                return 0
        return root
