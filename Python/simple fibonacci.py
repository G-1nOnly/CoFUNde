a, b = 0, 1
while b < 100:
    a, b = b, a + b
    print(b, '', end='')  # end控制在同一行
