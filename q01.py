##
## Imprima la suma de la segunda columna.
##
mail=open('data.csv','r').readlines()
mod=[int(row[2]) for row in mail]
print(sum(mod))
