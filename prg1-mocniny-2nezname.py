#vypiš mocniny dvou od 1-1024 za pomocí cyklu a 2 proměnných

cislo = 1  
mocnina = 0

while cislo <= 1024:
    print(cislo)
    mocnina += 1 
    cislo = 2 ** mocnina
    