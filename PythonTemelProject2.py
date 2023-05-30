def reorder(x):
    if isinstance(x, list) is True:
         if len(x) == 0:
             return []
         
         reord = reorder(x[len(x)-1])
         if isinstance(x[len(x)-1], list) is True:
             reord = [reord]
         
         return reord + reorder(x[0:len(x)-1])
    else:
         return [x]

m = [[1, 3], 2, [2,3]]
print(reorder(m))