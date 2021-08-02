import re

print(re.search(r'.', 'I love SJTU'))  # '.'匹配所有 加上r方便
print(re.search(r'S', 'I love SJTU'))
print(re.search(r'\d', 'I love SJTU2020'))  # '\d'表示数字
print(re.search(r'\d\d\d\d', 'I love SJTU2020'))  # 返回多个，一般只返回一个
print(re.search(r'[aeiou]', 'I love SJTU'))  # []一系列匹配
print(re.search(r'[a-z]', 'I love SJTU'))  # [x-y] 数字字母相同 限定范围
print(re.search(r'ab{3}c', 'abbbc'))  # 匹配多个{x} 重复次数x
print(re.search(r'[0-2][0-2][0-5]', '123456'))  # 0-255
# 正则表达式匹配字符串  故需要一个一个匹配
print(re.search(r'[^A-Z]', 'I love SJTU'))  # ^非
print(re.search(r'[0-2]|[4-5]|[7-9]', '36236'))  # |或
print(re.search(r'$', 'I love SJTU'))  # 匹配结束位置
print(re.findall(r'[a-z]', 'I love SJTU'))  # findall找到所有满足的
print(re.search(r'SJTU{1,3}', 'I love SJTU SJTU'))  # re{a,b} 匹配rea到b次
print(re.search(r'<.+>', '<I><LOVE><SJTU>'))
print(re.search(r'\bSJTU\b', 'I love SJTU'))  # \b匹配边界
a = re.search(r'(\w+) (\w+) (\w+)', 'I love SJTU')  # \w+匹配字符
print(a)
print(a.group())  # 将a打出
print(a.group(1), a.group(2), a.group(3))
