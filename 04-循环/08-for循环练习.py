"""
"""
"""
 小技巧 
   如果知道次数 建议使用for来完成 遍历容器用for 
   不知道次数,用while 写一个条件，比如>0
"""

# 求0-100偶数和===我的老办法
i =0
sum = 0
for i in range(0,101):
    if i % 2 == 0:   #愚蠢的老办法。可以用range步长来解决
        sum+=i

print(sum)

'''
求0-100偶数和====这是简单的方法，用range（起点，终点，步长）
'''
sum = 0
for i in range(0,101,2):
    sum += i
print(f'0-100的偶数和{sum}')

'''
用for循环
求 水仙花数的值 以及数量，更简单一些
'''
count = 0
for num in range(100,1000):
    ge = num % 10
    shi = num // 10 % 10
    bai = num // 100 % 10
    lifang = ge**3 + shi**3 + bai**3
    if lifang == num:
        count += 1
        print(num)
print(f'水仙花数有{count}个')

'''
对比
用while循环 
计数器要更新  ；但是for中的range函数默认步长为1
'''
# 1: 定义统计变量  以及 初始条件
count = 0
num = 100
# 2:实现循环
while num < 1000:
    # 满足条件统计
    ge = num % 10
    shi = num // 10 % 10
    bai = num // 100 % 10
    # 计算立方和
    lifang = ge**3 + shi**3 + bai**3
    if lifang == num : # 找到水仙花数
        count += 1   # 数量+1 =========================这里要记得，是写在if判断里面才对。
        print(num)  # 打印水仙花
    num += 1 # 继续下一个=======================这个在while循环中要写，计数器要更新；但是for中的range函数默认步长为1
# 3：循环结束 打印统计的结果
print(f'水仙花数有{count}个')