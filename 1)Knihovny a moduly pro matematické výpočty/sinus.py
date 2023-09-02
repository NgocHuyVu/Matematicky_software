import timeit
import numpy as np
import math

def reseni_pomoci_standardni_python(uhly):
    return [math.sin(uhel) for uhel in uhly]

def reseni_pomoci_numpy(uhly):
    return np.sin(uhly)

uhly = np.linspace(0, 2*np.pi, 100)

# Měření času pro standardní Python
python_cas = timeit.timeit(lambda: reseni_pomoci_standardni_python(uhly))
python_cas = round(python_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí standardního Pythonu: {python_cas} sekund")

# Měření času pro NumPy
numpy_cas = timeit.timeit(lambda: reseni_pomoci_numpy(uhly))
numpy_cas = round(numpy_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí NumPy: {numpy_cas} sekund")

#Porovnání: (stary_cas/novy_cas)/stary_cas*100
porovnani = round((python_cas-numpy_cas)/python_cas*100, 2)
print(f"Pomocí Numpy se vyřeší rychlejší o přiblížně {porovnani}%")
