# Remember that the quadratic equation is ax**2 + bx + c = 0
import cmath
a=float(input("Input a: "))
b=float(input("Input b: "))
c=float(input("Input c: "))

delta = b**2 + 4*a*c

x1=((-b-cmath.sqrt(delta))/(2*a))
x2=((-b+cmath.sqrt(delta))/(2*a))
print()
print("There are your solutions: {0}, {1}".format(x1,x2))
print()
print("I am happy to help you - anytime!")