import numpy as np

"""NUTNO MÍT NAINSTALOVANOU KNIHOVNU NUMPY V CMD!!!
 pip install numpy"""

znamky = np.array([[3,1], [3,2], [3,1], [10,3], [4,4]])


#Tady mi knihovna NumPy vybere jenom první index z každého listu (index 0), což jsou váhy u každé známky.

vaha = znamky[:, 0]


#Tady mi knihovna NumPy vybere jenom druhý index z každého listi (index 1), což jsou známky.
znamka = znamky[:, 1]


arit_prumer = np.sum(znamka) / np.count_nonzero(znamka)
print(arit_prumer)

vaz_prumer = np.sum(vaha * znamka) / np.sum(vaha)
print (vaz_prumer)

"""Vše jsem kontroloval podle kalkulačky

Při práci jsem používal ChatGPT jako pomoc s formmátem kódu a https://www.numpy.org/   pro vysvětlění funkcí """



