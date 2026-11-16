# 思路：直接当成字符串处理，支持任意大的自然数，不受整数范围限制
num_str = input("请输入一个自然数：")
sum_digit = 0
for char in num_str:
    sum_digit = sum_digit + int(char)
print("各位数字之和：", sum_digit)
