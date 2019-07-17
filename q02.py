##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
mod=([row[0] for row in mail])
for i in sorted(set(mod)): 
  z=mod.count(i)
  print(f"{i},{z}")
