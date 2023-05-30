def flatten(x):
    if isinstance(x, list) is True:
        if len(x) == 0:
            return []
        return flatten(x[0]) + flatten(x[1:])
    else:
        return [x]
    
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(a))