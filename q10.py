##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
mail=open('data.csv','r').readlines()
mail=[row.replace('\n','').split('\t') for row in mail]
b=[row[4].split(',') for row in mail]
n=','.join([row[4] for row in mail]).split(',')
n=[row.replace('\n','').split(':') for row in n]
n
mod=([row[0] for row in n])
for i in sorted(set(mod)):
  print(f"{i},{mod.count(i)}")
