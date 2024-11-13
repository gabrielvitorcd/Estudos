d1 = {
    'c1':1,
    'c2':2,
    'l1':[0,1,2],



}

d2 = d1.copy()  #shallow copy(copia)

d2['c1'] = 1000 
d2['l1'][1] = 9000      #esse codigo afeta as duas listas criadas, pois foi feita uma copia rasa

print(d1)
print(d2)