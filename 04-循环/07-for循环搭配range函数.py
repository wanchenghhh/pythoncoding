"""
"""

"""
  range() 函数介绍
  表示范围的
  搭配 for 循环使用！！
  for 循环 可以来遍历 range 指定的范围
"""
"""
  range函数 
    range() 本身可以返回第一个可以遍历(迭代)的对象

    range(结束值) 相当于 range(0,结束值)
    range(起始值,结束值)
    range(起始值,结束值,步长) 默认步长是1，每次变化 可以理解为是等差数列中的哪个差！

    range(5)    表示的范围 [0,1,2,3,4] 包前不包后  
    range(0,5)  表示的范围 [0,1,2,3,4] 包前不包后  
    range(1,8)  表示的范围 [1,2,3,4,5,6,7] 
    range(1,8,2)表示的范围 [1,3,5,7]  
    range(1,8,3)表示的范围 [1,4,7]  

    for 临时变量  in  range函数 
"""
for i in range(5):
    print(i ,end=' ')

print()

for i in range(1 ,8 ,2):
    print(i ,end=' ')

