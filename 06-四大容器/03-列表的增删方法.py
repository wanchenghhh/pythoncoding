"""
  列表中的增删
"""
"""
  增: 往列表中添加元素
     列表.append(元素) 将指定元素添加到列表中
     列表.insert(索引,元素) 将指定元素添加到列表的指定位置
     列表.extend(容器) 将容器中的所有元素添加当前列表中
"""
list1 = [1, 2, 3]
print(list1)  # [1,2,3]
# 追加
list1.append(5)
print(list1)  # [1, 2, 3, 5]
# 索引为3的位置插入4
list1.insert(3, 4)
print(list1)  # [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
# 整体添加到list1中
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8]
"""
  删除元素
     列表.pop() 弹出元素,不传参数,弹最右端元素  可以用变量接收或者是打印
     列表.pop(索引) 弹出指定位置的元素 可以用变量接收或者是打印
      列表.remove(元素)  删除指定的元素 不返回任何结果 注意搭配 in 语法 先做判断 再删除 否则报错
      列表.clear() 清空列表 
  删除列表
     del 列表名  删除指定列表 
     del 列表名[索引]  删除指定列表中指定索引的元素

"""
list3 = ["a", "b", "c", "d"]
print(f'list3.pop():{list3.pop()}')  # d
print(f'list3:{list3}')  # list3:['a', 'b', 'c']
print(f'list3.pop(1):{list3.pop(1)}')  # b
print(f'list3:{list3}')  # list3:['a', 'c']

list4 = ["高于", "高圆圆", "郑爽", "刘亦菲"]
list4.remove("高于")
print(f'list4:{list4}')  # list4:['高圆圆', '郑爽', '刘亦菲']
#  list4.remove("高于") # not in list
list4.clear()
print(f'list4:{list4}')  # list4:[]

# 删除 列表
del list4  # 删除整个列表
print(f'list4:{list4}')  # name 'list4' is not defined. Did you mean: 'list1'?