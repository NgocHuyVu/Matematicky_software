import random

def monte_carlo_simulace(pokus):
    tah_eso_srdce = 0
    
    for _ in range(pokus):
        karty = list(range(1, 14)) * 4
        random.shuffle(karty)
        
        if karty[0] == 1:  # eso srdce
            tah_eso_srdce += 1
    
    pravdepodobnost = (tah_eso_srdce  / pokus) * 100
    return pravdepodobnost

pokus = 100000  
vysledek = monte_carlo_simulace(pokus)

print(f"Pravděpodobnosti k vytažení eso srdce z 52 hracích karet je {vysledek} %")
