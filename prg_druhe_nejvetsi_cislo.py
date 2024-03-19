cisla = [4, 5, 3, 7, 8, 2, 1, 6]
nejvetsi = max(cisla[0], cisla[1])
druhe_nejvetsi = min(cisla[0], cisla[1])
for cislo in cisla[2:]:
    if cislo > nejvetsi:
        druhe_nejvetsi = nejvetsi
        nejvetsi = cislo
    elif cislo > druhe_nejvetsi:
        druhe_nejvetsi = cislo
print("Druhé největší číslo je:", druhe_nejvetsi)