# 输入一串数字，空格隔开
data = input("请输入一组数字，空格分隔：")
# 转为数字列表
lst = list(map(float, data.split()))

# 内置函数处理
max_val = max(lst)          # 最大值
lst_sorted = sorted(lst)    # 升序排序（内置sorted，返回新列表）
avg = sum(lst) / len(lst)   # 总和 / 长度 = 均值

# 输出
print(f"原始列表：{lst}")
print(f"升序排序后：{lst_sorted}")
print(f"最大值：{max_val}")
print(f"平均值：{avg:.2f}")
