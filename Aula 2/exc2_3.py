x = int(input())

def fib(n):
    prox = []
    result = [0]
    if (n<0):
        return
    if (n>0):
        result.append(1)
        while True:
            prox = result[-1] + result[-2]
            if prox > n:
                break
            result.append(prox)
    return result

def soma(l):
    result = 0
    for i in l:
        result += i
    return result
print (fib(x))
print (soma(fib(x)))