# 斐波那契函数
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a  # yield让该函数变成一个生成器
        a, b = b, a + b
        counter += 1


fib = fibonacci(10)  # fib是一个生成器
print(type(fib))
for i in fib:
    print(i, end=" ")  # end不换行
