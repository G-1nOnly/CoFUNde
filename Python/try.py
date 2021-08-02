a = int(input("0/1:"))
if a == 0:
    raise Exception("Exit!")  #raise+异常
#相当于assert a != 0 assert expression 相当于 if no expression  raise AssertionError

#try - except - else(无异常时执行） -finally（无论如何都执行）
# 可以有多个except 也可以一个except 中多个Error
while True:
    try:
        x = int(input("请输入一个数字: "))
    except Exception as reason:  # 捕获异常原因 利用str()打出 可有多个Exception
        print(str(reason))
    else:
        print(x)
        break
    finally:
        print("HELLO!")

