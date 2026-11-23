"""
 字典增删改查
"""
"""
字典是可变类型
  增 / 改
     字典名[key] = value  
          在字典中(键如果不存在)添加一个新的键值对 
          键如果存在，就完成值的更新
          
  删 
     字典名.pop(key) 根据键删除键值对      
     del 字典名[key] 根据键删除键值对   
     del 字典名      删除这个字典
     字典名.clear()  清空所有键值对     
"""
dict1 = {"李小璐":"贾乃亮","景田":"张继科"}
dict1['马蓉']='王宝强' # 新增
dict1['李小璐']='PGone' # 修改
print(dict1)
# 删除
print(f'pop之后:{dict1.pop("马蓉")}')  # pop之后:王宝强
print(dict1) #{'李小璐': 'PGone', '景田': '张继科'}

"""
   字典名[key]  字典名.get(key)  根据键找值 
   len(字典名)  获取字典中键值对的数量 
   字典名.keys()  获取所有的key
   字典名.values() 获取所有的值  
   字典名.items()  获取 每个键值对儿数据 注:每个键值对都做了封装 封装成元组 (键,值)
"""
print(dict1.keys()) # dict_keys(['李小璐', '景田'])
print(dict1.values())# dict_values(['PGone', '张继科'])
print(dict1.items()) # dict_items([('李小璐', 'PGone'), ('景田', '张继科')])
