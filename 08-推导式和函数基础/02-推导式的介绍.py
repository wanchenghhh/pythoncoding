"""
  推导式的使用

"""
"""
  推导式
    一种简洁 优雅的语法  用于创建数据的结构 
    其实就是 把符合要求的数据 推到指定的容器中 
    推导式 支持 列表 集合 字典 推导
    列表推导式基础语法 
       列表名 = [表达式 for 变量 in 容器/数据范围 ]
       从 容器/数据范围 中取出数据 使用 变量接收   根据表达式 推到到 新的列表中 
       表达式 指的是 你对 变量的处理方式

"""
# 需求
nums = []
# 把 1-100 数据 存到列表
for num in range(1, 101):
    nums.append(num)
print(nums)

# 列表名 = [表达式 for 变量 in 容器/数据范围 ]
nums2 = [num for num in range(1, 101)]
print(nums2)

#  求 1-10 的平方 推到 列表中
nums3 = [num ** 2 for num in range(1, 11)]
print(nums3)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 推导式进阶  列表名 = [表达式 for 变量 in 容器/数据范围  if 条件]
# 1-10 之间的偶数
nums4 = [num for num in range(1, 11) if num % 2 == 0]
print(nums4)  # [2, 4, 6, 8, 10]

# 进阶2  多重数据处理
# 列表名 = [表达式  for 变量1 in 容器/数据范围   for 变量2 in 容器/数据范围]
# 扑克牌   花色 数字
"♠♣♦♥"
"2345678910"
poker = [color + str(num) for color in "♠♣♦♥" for num in range(2, 11)]
print(poker)
print(len(poker))
