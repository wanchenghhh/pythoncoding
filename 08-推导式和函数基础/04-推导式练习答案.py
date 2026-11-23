"""
推导式练习
"""

# 1 使用列表推导式 取出 1-100中 所有 7的倍数
nums1 = [ i for i in range(1,101) if i % 7 == 0]
print(nums1)
# 2 使用列表推导式 完成 字符串处理把下面 单词变成大写
words = ["apple","banana","mango","pineapple"]
words2 = [ s.upper() for s in words]
print(words2)

# 3 使用列表推导式  只保留长度大于3的字符串
worldss = ["a","apple","hi","banana","cat"]
worlds2 = [s for s in worldss if len(s) > 3]
print(worlds2)

# 4 使用set集合推导式   保留大于2的数字 求立方 并实现去重
nums =[1,2,3,3,2,5,2]
set1 = {num**3  for num in nums if num >2}
print(set1)

# 5 找出所有字母  不能重复
text="hello java person hello"
set2 = {s for s in text if s!=' '}
print(set2)
"""
6 不难 不难  不难  想清楚 想不清楚 下一个
   双重循环 
      生成  两个列表中元素的所有组合
           [1,2,3]
           ['a','b']
     生成 元组 列表数据 --列表中包含元组  
     [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]   
        [表达式  for 变量1 in 容器  for 变量2 in 容器 ]
          表达式 可以对 变量1 变量2 进行处理 
"""
# 体现了打包
tuple_list = [(n,c) for n in [1,2,3] for c in ['a','b']]
print(tuple_list)

"""
  7 字典推导式  求 立方 1-10 键值信息
        { k:v for 变量 in 容器 }
        比如 
          1-10 
          key 数字 
          value  数字立方
       比如 1:1,2:8,3:27....   
"""
dict1 = {i:i**3 for i in range(1,11)}
print(dict1)
# 8 使用字典推导式 完成 信息筛选   保留分数大于60的学生
stu={"张三":80,"李四":55,"王五":90,"赵六":59}
dict2={ k:v  for k,v in stu.items() if v>60 }
print(dict2)

# 9 使用字典推导式 完成键值互换
dic = {"a":1,"b":2,"c":3}
dict4 = { v:k for k,v in dic.items() }
print(dict4)

# 10 使用字典推导式 统计字符出现次数    提示 set集合可以去重  字符串.count(字符) 可以直接求次数
#  生成字典 key 字符   value 出现次数
s="abracjashfga"
my_list = {c:s.count(c) for c in s}
print(my_list)
