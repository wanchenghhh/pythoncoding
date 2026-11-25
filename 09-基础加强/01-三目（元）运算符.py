"""
  讲解 三目运算符  和 macth-case
"""
"""
  三目运算符 三元运算符
    作用 
      在某些情况下 替换 if...else 甚至可以替换 if elif else 
    格式   
      真分支 if 条件 else 假分支   
    应用场景
      在推导式中使用  因为推导式就是一行代码！！
      在lambda中使用 因为lambda也是一行代码！！  
"""
#  1:满足18岁可以上网 不满足不可以上网
age = 14
print("可以上网") if age>=18 else print("不可以上网")


#  2.结合列表推导式使用
#  生成一个新列表，将原列表中的所有偶数除以 2，奇数保持不变。 [ 三元运算  for 变量 in 容器 ]
numbers = [12, 5, 8, 20, 3, 15, 7, 10]
new_numbers = [num/2 if num%2==0 else num for num in numbers]
print(new_numbers)

"""
  给你分数 设置一个等级
"""
score = 83
grade = ''  #没等级
# if score >= 90:
#     grade = 'A'
# elif score >= 75:
#     grade = 'B'
# elif score >= 60:
#     grade = 'C'
# else:
#     grade = 'D'
# 极力不建议！！ 因为可读性太差了
grade = 'A' if score >= 90 else  'B'  if score >= 75 else   'C' if score >= 60 else  'D'


print(grade)
