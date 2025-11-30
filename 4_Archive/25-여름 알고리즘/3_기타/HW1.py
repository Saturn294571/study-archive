def fibonacci(n):
    if n < 0:
        return "n은 음수일 수 없습니다."
    if n <= 1:
        return n
    f1, f2 = 0, 1
    for i in range(2, n + 1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn

for i in range(-2,10):
    print(f'{i}일때:',fibonacci(i))