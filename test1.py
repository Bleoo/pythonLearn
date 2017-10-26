L = list(range(10))
L[1:2] = [11, 22, 33, 44, 55]
print(L, 'with len =', len(L))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(10):
    print(n)


def yhsj(line):
    ol = list()
    for n in range(line):
        nl = list()
        for i in range(n + 1):
            if i == n or i == 0:
                nl.append(1)
            else:
                nl.append(ol[i - 1] + ol[i])
        ol = nl
        yield nl


for i in yhsj(10):
    print(i)


# 注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(lambda x: x % n > 0, it)  # 构造新序列  # 这个生成器先返回第一个素数2，然后，利用filter()


# 不断产生筛选后的新的序列。
# 由于primes()
# 也是一个无限序列，所以调用时需要设置一个退出循环的条件：

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
