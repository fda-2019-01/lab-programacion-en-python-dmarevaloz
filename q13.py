##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
mail=open('data.csv','r').readlines()
mail=[row.replace('\n','').split('\t') for row in mail]
mail=[[row[0],row[4].split(',')] for row in mail]
for row in mail:
  b=0
  for k in range(len(row[1])):
    for i in range(10):  
      if str(i) in row[1][k]: 
         b+=i
  print(f'{row[0]},{b}')
