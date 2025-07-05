import math

class Fraction:
    def __init__(self, x, y, show_menu=False):
               self.num = x
               self.denom = y
               if show_menu:
                   self.menu()

    def __str__(self):
               return f"{self.num}/{self.denom}"

    def __add__(self, other):
               new_num = self.num * other.denom + other.num * self.denom
               new_denom = self.denom * other.denom
               return Fraction(new_num, new_denom, show_menu=False)

    def __sub__(self, other):
               new_num = self.num * other.denom - other.num * self.denom
               new_denom = self.denom * other.denom
               return Fraction(new_num, new_denom, show_menu=False)

    def __mul__(self, other):
               new_num = self.num * other.num
               new_denom = self.denom * other.denom
               return Fraction(new_num, new_denom, show_menu=False)

    def __truediv__(self, other):
               new_num = self.num * other.denom
               new_denom = self.denom * other.num
               return Fraction(new_num, new_denom, show_menu=False)

    def convert_to_decimal(self):
               return self.num / self.denom

    def simplify(self):
               gcd = math.gcd(self.num, self.denom)
               self.num = self.num // gcd
               self.denom = self.denom // gcd
               return self

    def mixed(self):
               if self.num < self.denom:
                   return str(self)
               quotient = self.num // self.denom
               remainder = self.num % self.denom
               return f"{quotient} ({remainder}/{self.denom})"

    def to_float(self, place):
               deci = self.num / self.denom
               return f"{deci:.{place}f}"

    @classmethod
    def conversion(cls, quotient, remainder, denom):
               new_num = denom * quotient + remainder
               return cls(new_num, denom, show_menu=False)

    def menu(self):
               func = input("""
               1. Print in Format
               2. Addition
               3. Subtraction
               4. Multiplication
               5. Division
               6. Convert to Decimal
               7. Simplify
               8. Mixed Number
               9. Float with Precision
               10. Convert Mixed to Fraction
               """)

               if func == "1":
                   print("Formatted:", str(self))
               elif func in ["2", "3", "4", "5"]:
                   x = int(input("Enter numerator of second fraction: "))
                   y = int(input("Enter denominator of second fraction: "))
                   other = Fraction(x, y, show_menu=False)
                   if func == "2":
                       print("Addition:", self + other)
                   elif func == "3":
                       print("Subtraction:", self - other)
                   elif func == "4":
                       print("Multiplication:", self * other)
                   elif func == "5":
                       print("Division:", self / other)
               elif func == "6":
                   print("Decimal:", self.convert_to_decimal())
               elif func == "7":
                   print("Simplified:", self.simplify())
               elif func == "8":
                   print("Mixed Number:", self.mixed())
               elif func == "9":
                   place = int(input("Decimal places: "))
                   print("Float Precision:", self.to_float(place))
               elif func == "10":
                   q = int(input("Whole number: "))
                   r = int(input("Numerator: "))
                   d = int(input("Denominator: "))
                   print("Converted Fraction:", Fraction.conversion(q, r, d))
               else:
                   print("Invalid option")

class Point:
    show_menu = True

    def __init__(self, x, y):
         self.x_cod = x
         self.y_cod = y

         if Point.show_menu:
            self.menu()

    def __str__(self):
        return "<{},{}>".format(self.x_cod, self.y_cod)

    def euclidean_dist(self, other):
         return ((self.x_cod - other.x_cod) ** 2 + (self.y_cod - other.y_cod) ** 2) ** 0.5

    def dist_from_origin(self):
                    return self.euclidean_dist(Point(0, 0))

    def mid_point_2_point(self, other):
        return ((self.x_cod + other.x_cod) / 2, (self.y_cod + other.y_cod) / 2)

    def slope_bw_2_points(self, other):
        try:
            slope = (self.y_cod - other.y_cod) / (self.x_cod - other.x_cod)
            return slope
        except ZeroDivisionError:
            return "Undefined (vertical line)"

    def quadrant_finder(self):
        if self.x_cod > 0 and self.y_cod > 0:
                        return "First Quadrant"
        elif self.x_cod > 0 and self.y_cod < 0:
                        return "Fourth Quadrant"
        elif self.x_cod < 0 and self.y_cod > 0:
                        return "Second Quadrant"
        elif self.x_cod < 0 and self.y_cod < 0:
                        return "Third Quadrant"
        elif self.x_cod == 0 and self.y_cod == 0:
                        return "Origin"
        elif self.x_cod == 0:
                        return "Y-axis"
        elif self.y_cod == 0:
                        return "X-axis"

    def menu(self):
        Point.show_menu = False
        user_input = input("""
            Hey! What do you want to know?
            1. Distance Between 2 Points
            2. Distance From Origin
            3. Mid Point Between 2 Points
            4. Slope Between 2 Points
            5. Quadrant Finder
            → Your Choice: """)

        if user_input == "2":
                        print("Distance From Origin:", self.dist_from_origin())
        elif user_input == "5":
                        print("Quadrant of the point is:", self.quadrant_finder())
        elif user_input in ["1", "3", "4"]:
                        x2 = int(input("Enter second point's x: "))
                        y2 = int(input("Enter second point's y: "))
                        other = Point(x2, y2)

                        if user_input == "1":
                            print("Distance between the points is:", self.euclidean_dist(other))
                        elif user_input == "3":
                            print("Midpoint between the given points is:", self.mid_point_2_point(other))
                        elif user_input == "4":
                            slope = self.slope_bw_2_points(other)
                            print("Slope between given points is:", slope)
        else:
                        print("Invalid option.")


class Line:
    show_menu = True

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

        if Line.show_menu:
            self.menu()

    def __str__(self):
                return "{}x + {}y + {}".format(self.A, self.B, self.C)

    def point_on_line(self, point):
                if self.A * point.x_cod + self.B * point.y_cod + self.C == 0:
                    return True
                return False

    def shortest_dist(self, point):
                return abs(self.A * point.x_cod + self.B * point.y_cod + self.C) / ((self.A ** 2 + self.B ** 2) ** 0.5)

    def slope_line(self):
                try:
                    return -self.A / self.B
                except ZeroDivisionError:
                    return "Undefined"

    def y_intercept(self):
                try:
                    return -self.C / self.B
                except ZeroDivisionError:
                    return "Undefined"

    def menu(self):
                Line.show_menu = False
                option = input("""
        What do you want to do with this line?
        1. Shortest Distance from a Point to the Line
        2. Check if a Point lies on the Line
        3. Slope of Line
        4. Y-Intercept
        → Your Choice: """)

                if option == "3":
                    print("Slope of the line is:", self.slope_line())
                elif option == "4":
                    print("Y-Intercept is:", self.y_intercept())
                elif option in ["1", "2"]:
                    x = int(input("Enter point's x: "))
                    y = int(input("Enter point's y: "))
                    point = Point(x, y)

                    if option == "1":
                        print("Shortest Distance:", self.shortest_dist(point))
                    elif option == "2":
                        print("Is point on line:", "Yes" if self.point_on_line(point) else "No")
                else:
                    print("Invalid option.")



class Polynomial:
    def __init__(self, coeffs, show_menu=True):
        self.coeffs = coeffs
        if show_menu:
            self.menu()

    def __str__(self):
        result = ""
        degree = len(self.coeffs) - 1
        for i, coef in enumerate(self.coeffs):
            if coef == 0:
                continue
            power = degree - i
            if power == 0:
                result += f"{coef}"
            elif power == 1:
                result += f"{coef}x + "
            else:
                result += f"{coef}x^{power} + "
        return result.rstrip(" + ")

    def __add__(self, other):
        len_1 = len(self.coeffs)
        len_2 = len(other.coeffs)

        if len_1 < len_2:
            padded_self = [0] * (len_2 - len_1) + self.coeffs
            padded_other = other.coeffs
        else:
            padded_other = [0] * (len_1 - len_2) + other.coeffs
            padded_self = self.coeffs

        result = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result, show_menu=False)

    def __sub__(self, other):
        len_1 = len(self.coeffs)
        len_2 = len(other.coeffs)

        if len_1 < len_2:
            padded_self = [0] * (len_2 - len_1) + self.coeffs
            padded_other = other.coeffs
        else:
            padded_other = [0] * (len_1 - len_2) + other.coeffs
            padded_self = self.coeffs

        result = [a - b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result, show_menu=False)

    def __mul__(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)

        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(result, show_menu=False)

    def __truediv__(self, other):
        dividend = self.coeffs[:]
        divisor = other.coeffs[:]
        quotient = []

        while len(dividend) >= len(divisor):
            lead_coeff = dividend[0] / divisor[0]
            deg_diff = len(dividend) - len(divisor)

            # Build the current subtractor
            subtractor = [lead_coeff * c for c in divisor] + [0] * deg_diff

            # Add to quotient
            if len(quotient) == 0:
                quotient = [0] * (deg_diff + 1)
            quotient[deg_diff] = lead_coeff

            # Subtract from dividend
            dividend = [a - b for a, b in zip(dividend + [0]*(len(subtractor)-len(dividend)), subtractor)]

            # Remove leading zeros
            while dividend and dividend[0] == 0:
                dividend.pop(0)

        return Polynomial(quotient, show_menu=False)

    def menu(self):
        user_input = input("""
💡 What would you like to do?
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Display it
→ Your Choice: """)

        if user_input == "5":
            print("Polynomial:", self)

        elif user_input in ["1", "2", "3", "4"]:
            try:
                other_coeffs = list(map(int, input("Enter coefficients of the other polynomial (space-separated): ").split()))
                other = Polynomial(other_coeffs, show_menu=False)

                if user_input == "1":
                    result = self + other
                    print("Addition Result:", result)
                elif user_input == "2":
                    result = self - other
                    print("Subtraction Result:", result)
                elif user_input == "3":
                    result = self * other
                    print(" Multiplication Result:", result)
                elif user_input == "4":
                    result = self / other
                    print(" Division Result:", result)
            except Exception as e:
                print("Error:", e)
        else:
            print(" Invalid choice. Try again.")