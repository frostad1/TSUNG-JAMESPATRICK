a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if ((a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b)):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")