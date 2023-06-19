import numpy as np
import timeit

# Standardní Python
def pomoci_standardniho_pythonu(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

# NumPy
def pomoci_numpy(a, b):
    return np.dot(a, b)

# Generování dat
a = np.random.rand(1000000)
b = np.random.rand(1000000)


# Měření času pro standardní Python
python_cas = timeit.timeit(lambda: pomoci_standardniho_pythonu(a, b), number=100)
python_cas = round(python_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí standardního Pythonu: {python_cas} sekund")

# Měření času pro NumPy
numpy_cas = timeit.timeit(lambda: pomoci_numpy(a, b), number=100)
numpy_cas = round(numpy_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí NumPy: {numpy_cas} sekund")

#Porovnání: (stary_cas/novy_cas)/stary_cas*100
porovnani = round((python_cas-numpy_cas)/python_cas*100, 2)
print(f"Pomocí Numpy se vyřeší rychlejší o přiblížně {porovnani}%")