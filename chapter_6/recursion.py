# _*_ coding:utf-8 _*_
# 阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 幂
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


# 二分查找
def search(sequence, number, lower = 0, upper = None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper] # 断言
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)
seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print seq
print search(seq, 34)
print search(seq, 100)
print search(seq, 123)