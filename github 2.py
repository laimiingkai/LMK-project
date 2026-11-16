# 获取用户输入，转成集合
# 输入示例：1 2 3 4
a_input = input("请输入集合A的元素，用空格隔开：")
b_input = input("请输入集合B的元素，用空格隔开：")

# 分割字符串，转为集合
set_a = set(a_input.split())
set_b = set(b_input.split())

# 计算
inter = set_a & set_b      # 交集
union = set_a | set_b      # 并集
diff_a = set_a - set_b     # A-B：属于A不属于B
diff_b = set_b - set_a     # B-A：属于B不属于A

# 输出
print(f"集合A：{set_a}")
print(f"集合B：{set_b}")
print(f"交集：{inter}")
print(f"并集：{union}")
print(f"A - B（A的差集）：{diff_a}")
print(f"B - A（B的差集）：{diff_b}")
