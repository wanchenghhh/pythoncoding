"""
  列表的改查方法
     修改列表中的元素  查询列表中的元素
"""
"""
 所有操作使用到 索引的地方 如果填写索引不存在就会报错！！！

  列表中改的功能
     列表[索引] = 新值 
     二维列表 
       列表[第一层索引][第二层索引] = 新值  

     列表.sort() 按照自然顺序排序 升序
     列表.sort(reverse=True) 按照自然顺序降序排列 
     列表.reverse() 实现列表中元素反转  

"""
# 简单的修改
list1 = ["樊振东", "王楚钦", "梁靖崑", "方博"]
list1[0] = '小胖'
print(list1)  # ['小胖', '王楚钦', '梁靖崑', '方博']
# 高级的修改  排序有关系
list2 = [5, 7, 2, 4, 8, 3]
# 可以进行排序
list2.sort()  # 实现 列表中元素 排序 升序
print(list2)  # [2, 3, 4, 5, 7, 8]
# 想降序怎么办？
list2.reverse()  # 列表中的数据 全部反转
print(list2)  # [8, 7, 5, 4, 3, 2]

# sort使用的时候 加入参数  reverse=True 降序
list3 = [5, 7, 2, 4, 8, 3]
list3.sort(reverse=True)  # reverse 是不是需要排序反转  升序-降序
print(list3)  # [8, 7, 5, 4, 3, 2]
print("=" * 100)
"""
  查  
    元素 in 列表  判断元素在不在列表中  返回 True False
    元素 not in 列表 不在  
    列表.count(元素)  指定元素在列表中出现的次数 没有就是0 
    列表.index(元素)  找到元素在列表中出现的位置(索引) 找不到报错
"""
name_list = ['迪丽热巴', '古力娜扎', '马尔扎哈', '哈妮克孜', '马尔扎哈']
print(f'热巴在不在列表中:{"热巴" in name_list}')
print(f'迪丽热巴在不在列表中:{"迪丽热巴" in name_list}')
print(f'马尔扎哈在列表中出现的次数:{name_list.count('马尔扎哈')}')
print(f'马尔扎哈在列表中出现第一次出现的位置:{name_list.index('马尔扎哈')}')

"""
  列表中通用的 全局函数 
  len(列表) 查看列表的长度
  max(列表) 求最大元素  min(列表) 求最小元素 sum(列表) 求和 avg?
  max(元素1,元素2) 求最大元素
  sort(列表)
  sort(列表,reverse=True)

"""

num_list = [27000, 27500, 30000, 24300]
print(f'最高薪资:{max(num_list)}')
print(f'最低薪资:{min(num_list)}')
print(f'总薪资:{sum(num_list)}')
print(f'平均薪资:{sum(num_list) / len(num_list)}')

"""
 列表的扩充
"""
list5 = list1 + list2
print(list5)

list4 = ['火影忍者', '柯南', '海贼王', '七龙珠']
print(list4 * 2)
