num = input("请输入一个三位正整数：")
if len(num) == 3 and num.isdigit():
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    s = a + b + c
    print(f"{a}+{b}+{c}={s}")
else:
    print("输入不对，请输入3位数字！")
input("按回车关闭窗口")
