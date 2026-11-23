"""
  元组的练习
"""
tuple2= ((1,2,3),(2,4,6),(2,3,5))
# 实现元组的 遍历  拿到每个元素存到列表中(不重复的 升序)
# 创建新的列表
new_list = []
# 用for 遍历二维的元组
for tuple1 in tuple2:  # 把一维的元组遍历出来
    # tuple1是一维元组
    for item in tuple1:
        if item not in new_list:
            new_list.append(item)
print(f'没有排序的列表{new_list}')
# 得到 new_list 里面不重复但是 没有排序
# 排序
new_list.sort()
print(new_list)