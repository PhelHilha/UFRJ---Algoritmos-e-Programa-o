a = eval(input())
b = int(input())

def recurbinario(x, y, i, j):
    if i > j:
        return -1
    
    m = (i + j) // 2
    
    if x[m] == y:
        return m
    elif x[m] < y:
        return recurbinario(x, y, m + 1, j)
    else:
        return recurbinario(x, y, i, m - 1)

def buscar(x, y):
    return recurbinario(x, y, 0, len(x) - 1)
    
print(buscar(a,b))