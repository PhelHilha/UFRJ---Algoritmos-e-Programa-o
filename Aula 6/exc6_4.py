a = eval(input())

def recurbinario(x, y, i, j):
    if i > j:
        return i
    
    m = (i + j) // 2
    
    if x[m] == y:
        return m
    elif x[m] < y:
        return recurbinario(x, y, m + 1, j)
    else:
        return recurbinario(x, y, i, m - 1)
def ordenar(l):
    v = []
    
    for x in l:
        idx = recurbinario(v, x, 0, len(v) - 1)

        
        v.insert(idx, x)
    
    return v


print(ordenar(a))