# _*_ coding:utf-8 _*_
# 列表推导式是利用其他列表创建新列表的一种方法。
print[x * x for x in range(10)]
print[x * x for x in range(10) if x % 3 == 0]

print[(x, y) for x in range(3) for y in range(3)]
result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
# 得到名字首字母相同的男孩跟女孩
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print[b + '+' + g for b in boys for g in girls if b[0] == g[0]]
# 更优秀的方案
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {} # 创建一个letterGirl的字典
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print[b + '+' + g for b in boys for g in letterGirls[b[0]]]
