import sympy as sp
import timeit

# Symbolická proměnná
x = sp.symbols('x')

zadani = input("Zadejte funkci f(x) např. x**2 + 2*x + 1 : ")

try:
    f = sp.sympify(zadani)
except sp.SympifyError:
    print("Chyba při zpracování vstupu.")
    exit(1)

# interval určítého inegrálu (a,b)
a = 1
b = 5

# Definice funkce pro výpočet určitého integrálu pomocí SymPy
def pomoci_sympy():
    return sp.integrate(f, (x, a, b))

# Definice funkce pro výpočet určitého integrálu standardním Pythonem
def pomoci_strandardniho_python():
    # Definice diskretizace intervalu a krok pro sumaci
    n = 10000
    dx = (b - a) / n

    # Sumace hodnot funkce na diskretizovaném intervalu
    integral = sum(f.subs(x, a + i * dx) for i in range(n))

    # Násobení krokem pro výpočet určitého integrálu
    return integral * dx

# Měření času pro standardní Python
python_cas = timeit.timeit(lambda: pomoci_strandardniho_python)
print(f"Potřebný čas pro vyřešení pomocí standardního Pythonu: {python_cas} sekund")

# Měření času pro NumPy
numpy_cas = timeit.timeit(lambda: pomoci_sympy)
print(f"Potřebný čas pro vyřešení pomocí SymPy: {numpy_cas} sekund")

#Porovnání: (stary_cas/novy_cas)/stary_cas*100
porovnani = round((python_cas-numpy_cas)/python_cas*100, 2)
print(f"Pomocí Numpy se vyřeší rychlejší o přiblížně {porovnani}%")
