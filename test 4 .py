# 输入
lstA = list(map(int, input("请输入列表A，空格分隔：").split()))
lstB = list(map(int, input("请输入列表B，空格分隔：").split()))
# 取较短长度
n = min(len(lstA), len(lstB))
d = {}
for i in range(n):
    d[lstA[i]] = lstB[i]
print(d)


lst = list(map(int, input("请输入整数列表，空格分隔：").split()))
new_lst = sorted(lst, reverse=True)
print(new_lst)

lst = list(map(int, input("请输入整数列表，空格分隔：").split()))
res = 1
for num in lst:
    res *= num
print("连乘结果：", res)

p1 = list(map(int, input("输入第一个坐标 x y：").split()))
p2 = list(map(int, input("输入第二个坐标 x y：").split()))
dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print("曼哈顿距离：", dist)
