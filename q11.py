##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
mail=open('data.csv','r').readlines()
mail=[row.replace('\n','').split('\t') for row in mail]
mail=[[row[0], row[3].split(','), row[4].split(',')] for row in mail]
for i in mail: 
  print(f'{i[0]},{len(i[1])},{len(i[2])}')
