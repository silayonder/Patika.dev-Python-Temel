# m = [[1, 3], 2, [2,3]]
# m2  = []
# for l in m:
#     for e in l:
#         m2.append(e)
# print(m2)


def flatten(x):
    if isinstance(x, list) is True:
        if len(x) == 0:
            return []
        return flatten(x[0]) + flatten(x[1:])
    else:
        return [x]
    
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(a))