"""
"""
"""
  元组:
     是一个不可变的且有序的 数据的容器
  创建元组的方式
    元组名=(元素1,元素2...)
    元组名=(元素1,)
    空元组
      元组名=()
      元组名=tuple()
"""

# 定义元组 表达 某个同学
person = (1,'法外狂徒小桐','男')
print(person,type(person)) # (1, '法外狂徒小桐', '男') <class 'tuple'>

# 元组中的元素不可变 ，但可以访问。tup1[1]
print(f'查看person中的名字:{person[1]}')

# person[2]='TS'  元组中的元素不能变

data=(1,2,3,2,1,3) # 可以存储重复的

# count()    tup1.count(2)
print(f'查看2出现的次数:{data.count(2)}') # 查看2出现的次数:2

# index()      tup1.index(2)
print(f'查看2出现的第一个索引:{data.index(2)}') # 查看2出现的第一个索引:1

# in           2 in tup1
print(f'查看有没有2:{2 in data}') # 查看有没有2:True

# 开发用元组干什么 存储不变的一组数据 比如 坐标
bj=(39.9,116.3)
xian=(34,108)

# 删除
del xian
