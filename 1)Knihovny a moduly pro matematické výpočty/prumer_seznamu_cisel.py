import statistics
import timeit
import numpy as np

# Standardní Python
def pomoci__strandardniho_python(data):
    return statistics.mean(data)

# NumPy
def pomoci_numpy(data):
    return np.mean(data)

# Měření času pro standardní Python
python_cas = timeit.timeit(lambda: pomoci__strandardniho_python(np.random.rand(1000000)), number=50)
print(f"Potřebný čas pro vyřešení pomocí standardního Pythonu: {python_cas} sekund")

# Měření času pro NumPy
numpy_cas = timeit.timeit(lambda: pomoci_numpy(np.random.rand(1000000)), number=50)
print(f"Potřebný čas pro vyřešení pomocí NumPy: {numpy_cas} sekund")

#Porovnání: (stary_cas/novy_cas)/stary_cas*100
porovnani = round((python_cas-numpy_cas)/python_cas*100, 2)
print(f"Pomocí Numpy se vyřeší rychlejší o přiblížně {porovnani}%")