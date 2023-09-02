import timeit
import numpy as np

n = 100
# Standardní Python
def reseni_pomoci_standardni_python(n):
    vysledek = 1
    for i in range(1, n+1):
        vysledek *= i
    return vysledek

def reseni_pomoci_numpy(n):
    return np.prod(np.arange(1, n+1))

# Měření času pro standardní Python
python_cas = timeit.timeit(lambda: reseni_pomoci_standardni_python(n))
python_cas = round(python_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí standardního Pythonu: {python_cas} sekund")

# Měření času pro NumPy
numpy_cas = timeit.timeit(lambda: reseni_pomoci_numpy(n))
numpy_cas = round(numpy_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí NumPy: {numpy_cas} sekund")

#Porovnání: (stary_cas/novy_cas)/stary_cas*100
porovnani = round((python_cas-numpy_cas)/python_cas*100, 2)
print(f"Pomocí Numpy se vyřeší rychlejší o přiblížně {porovnani}%")

