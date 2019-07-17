##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
mail=open('data.csv','r').readlines()
mail = [row.split('-') for row in mail]
mod=([row[1] for row in mail])
for i in sorted(set(mod)):
  print(f"{i},{mod.count(i)}")
