n = int(input())

def f_lazy_fibonacci():
    prox = []
    result = [0]
    yield 0
    result.append(1)
    yield 1
    while True:
        prox = result[-1] + result[-2]
        result.append(prox)
        yield (prox)


for i,x in enumerate(f_lazy_fibonacci()):

    if i >= n:   break

    print(x,end=' ')