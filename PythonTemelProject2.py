# def reorder(x):
#     if isinstance(x, list) is True:
#         if len(x) == 0:
#             return []
#         return reorder(x[0]) + flatten(x[1:])
#     else:
#         return [x]
    
# a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# print(reorder(a))


m = [[1, 3], 2, [2,3]]
m2  = []

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

print(reorder(m))


# for i in range(len(m)):
#     m2.append(m[len(m)-i-1])
# print(m2)