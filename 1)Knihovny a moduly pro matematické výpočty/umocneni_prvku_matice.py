import timeit
import numpy as np

def reseni_pomoci_standardni_python(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[i][j] ** 2
    return result

def reseni_pomoci_numpy(matrix):
    return np.square(matrix)


matice = np.random.rand(10, 10)
# Měření času pro standardní Python
python_cas = timeit.timeit(lambda: reseni_pomoci_standardni_python(matice))
python_cas = round(python_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí standardního Pythonu: {python_cas} sekund")

# Měření času pro NumPy
numpy_cas = timeit.timeit(lambda: reseni_pomoci_numpy(matice))
numpy_cas = round(numpy_cas, 2)
print(f"Potřebný čas pro vyřešení pomocí NumPy: {numpy_cas} sekund")

#Porovnání: (stary_cas/novy_cas)/stary_cas*100
porovnani = round((python_cas-numpy_cas)/python_cas*100, 2)
print(f"Pomocí Numpy se vyřeší rychlejší o přiblížně {porovnani}%")