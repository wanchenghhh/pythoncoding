"""
  集合的定义和使用
"""
"""
  set 集合:
     是一个无序且元素不重复的 容器 
  集合的定义
      set1 = {元素1,元素2...}
      set2 = set()   #不能用{}表示空，因为这个是字典
  特点：
    元素唯一 无序
    元素类型 整数 浮点数 布尔值 字符串 元组
    长度可变   
"""
# 定义 set集合
set1= set()
print(type(set1)) # <class 'set'>

set2 = {1,2,3,4,2,1,5}
print(f'len(set2):{len(set2)}')# len(set2):5  实现去重了
print(f'set2:{set2}')# set2:{1, 2, 3, 4, 5}


"""
  添加 add(元素)  把元素添加到集合中
  set1.add(元素)
"""
qlz = {'孙悟饭','孙悟空','孙悟天','牛魔王','龟仙人'}
print(f'qlz:{qlz}')

# 添加元素   集合名.add()
qlz.add('贝吉塔')
qlz.add('铁扇公主')
print(f'qlz:{qlz}') # qlz:{'贝吉塔', '龟仙人', '孙悟空', '铁扇公主', '孙悟天', '牛魔王', '孙悟饭'}


"""
  删除 
   set1.remove(元素) 删除指定元素
   set1.pop() 随机删 返回被删除元素
   set1.clear() 清空 集合 
   del 集合 删除集合 
"""

qlz.remove('孙悟空')
print(f'qlz:{qlz}') # qlz:{'孙悟饭', '牛魔王', '铁扇公主', '贝吉塔', '龟仙人', '孙悟天'}
print(f'qlz里面随机死一个:{qlz.pop()}') # qlz里面随机死一个:铁扇公主
print(f'qlz:{qlz}')# qlz:{'孙悟饭', '牛魔王', '贝吉塔', '孙悟天', '龟仙人'}
qlz.clear() # 清空
del qlz  # 删除 集合

print("========能不能当成数学中的集合看待 =========")


gui_chui_deng = {"胡八一","王胖子","金牙","雪松"}
dao_mu_bi_ji = {"吴邪","王胖子","张起灵","雪松"}

# 交集 intersection
print(f'gui_chui_deng & dao_mu_bi_ji : {gui_chui_deng & dao_mu_bi_ji}')
print(f'gui_chui_deng.intersection(dao_mu_bi_ji) : {gui_chui_deng.intersection(dao_mu_bi_ji)}')
# print(f'如果加了update 表示做数据的更新，将结果更新到调用者上 : {gui_chui_deng.intersection_update(dao_mu_bi_ji)}')
# print(gui_chui_deng)

# 并集 union
print(f'gui_chui_deng | dao_mu_bi_ji : {gui_chui_deng | dao_mu_bi_ji}')  # {'吴邪', '胡八一', '张起灵', '金牙', '雪松', '王胖子'}
print(f'gui_chui_deng.union(dao_mu_bi_ji) : {gui_chui_deng.union(dao_mu_bi_ji)}') # {'吴邪', '胡八一', '张起灵', '金牙', '雪松', '王胖子'}

# 差集difference
print(f'gui_chui_deng - dao_mu_bi_ji : {gui_chui_deng - dao_mu_bi_ji}')# gui_chui_deng - dao_mu_bi_ji : {'胡八一', '金牙'}
print(f'gui_chui_deng.difference(dao_mu_bi_ji) : {gui_chui_deng.difference(dao_mu_bi_ji)}') # gui_chui_deng.difference(dao_mu_bi_ji) : {'胡八一', '金牙'}




