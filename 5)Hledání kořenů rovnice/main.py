import math

# polynom 3. stupně: f(x) = x^3 - 3x + 1
def bisection(f, a, b, tol=1e-6, max_iter=100):
    i = 0
    while i < max_iter:
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
    return None

def f1(x):
    return x ** 3 - 3 * x + 1

a = -2
b = 0
root1 = bisection(f1, a, b)
print("Kořen funkce f1 nalezený metodou půlení intervalu: ", root1)

# exponenciální funkce: f(x) = e^x - 3x
def f2(x):
    return math.exp(x) - 3 * x

a = 0
b = 1
root2 = bisection(f2, a, b)
print("Kořen funkce f2 nalezený metodou půlení intervalu: ", root2)

# trigonometrická funkce: f(x) = sin(x) + x/2
def f3(x):
    return math.sin(x) + x/2

a = -1
b = 1
root3 = bisection(f3, a, b)
print("Kořen funkce f3 nalezený metodou půlení intervalu: ", root3)
