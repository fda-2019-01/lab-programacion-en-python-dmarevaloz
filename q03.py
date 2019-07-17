##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
mail=open('data.csv','r').readlines()
mail=[row.split('\t') for row in mail]
a=dict()
for row in mail: 
  if row[0] not in a.keys():
    a[row[0]]=0
  a[row[0]]=a[row[0]]+int(row[1])
for i in sorted(a.keys()):
  print(i,',',a[i],sep='')
