import re

s = "['455', '万']"
# a = eval(s)
a = re.sub(r'\[|\]', "", s)
print(a)


def a(i):
    return i ** 2


L = [a(i) for i in range(1, 11) if i ** 2 > 50]
# L = [a(i) if i ** 2 > 50 else 100 for i in range(1, 11)]
print(L)

a = '100'
# c = "'455'"
# b = int(c)
# print(b)

d = '高楼层'

print(d.find('高'))
print(d.find('1'))

aa = '12(345)6 '
# re.match(r'\([\s\S]+\)')
bb = re.sub(r'(\([\s\S]+\))', "",aa).strip()
print(bb)


