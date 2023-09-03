import numpy as np
import time
import matplotlib.pyplot as plt

def vyreseni_matic(velikost_matic):
    matice = np.random.rand(velikost_matic, velikost_matic)  # náhodná matice
    result = np.linalg.det(matice) # Determinant matic
    time.sleep(velikost_matic)
    return result

velikost_matic = list(range(1, 5))  # Velikosti matic od 1x1 do 10x10
prumerny_cas = []

for size in velikost_matic:
    casy = []
    for i in range(5):  # Opakovaně řešit pro každou velikost matice a vzít průměr
        start = time.time()
        vyreseni_matic(size)
        end = time.time()
        casy.append(end - start)
    prumerny_cas.append(np.mean(casy))  

# Vykreslení grafu
plt.plot(velikost_matic, prumerny_cas, marker='o')
plt.title('Průměrný čas řešení v závislosti na velikosti matice')
plt.xlabel('Velikost matice')
plt.ylabel('Průměrný čas (s)')
plt.grid(True)
plt.show()
