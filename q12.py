##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
mail=open('data.csv','r').readlines()
mail=[row.split('\t') for row in mail]
mail=[[row[3].split(','), row[1]] for row in mail]
a=dict()
for row in mail: 
  for k in range(len(row[0])):
    if row[0][int(k)] not in a.keys():
      a[row[0][int(k)]]=0
    a[row[0][int(k)]]=a[row[0][int(k)]]+int(row[1])
for i in sorted(a.keys()):
  print(i,',',a[i],sep='')
