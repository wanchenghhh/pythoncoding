"""
  统计缺失值
"""
"""
编写一个程序来统计缺失的数字并返回它们的总和。缺失的数字是指给定列表中两个极端（最大和最小数字）之间没有出现的数字。
例如，给列表{2, 5, 3, 7, 5, 7}中，两个极端（即2和7）之间缺失的数字是4和6。
"""
#1:定义一个 集合
numbers=[2, 5, 3, 7, 5, 7]
# 列表变集合
number_set = set(numbers)

# 2：求最大值  最小值
max_number = max(numbers)
min_number = min(numbers)

# 3 范围内求
# 定义求个变量
missing_sum = 0
# 范围变量 min_number+1  max_number
for num in range(min_number+1, max_number):
    # 不在的就是缺失值
    if num not in number_set:
       missing_sum += num
print(missing_sum)