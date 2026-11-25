"""
  主要讲
    位置参数
    关键字参数
    混用
"""
"""
 在python中 做参数传递，主要有以下几种方式
   1:位置参数:调用函数的时候，根据形参的"位置"进行参数的传递。
            要求: 实参的位置 和 形参的位置 要一一对应 。
   2:关键字参数: 调用参数逇时候,根据形参的名字进行传参(key=value)。
            要求: 形参的名字和实参的key 一一对应        
   3:混用  要求  位置参数一定在前面！！！    
   4:解包传参   元组传参--位置传参      * 解包
               字典---关键字传参  key 和形参名一致   **解包
"""
# 定义函数
def print_info(name,age,address):
    print(f'姓名:{name},年龄:{age},住址:{address}')

# 1:使用 位置参数  完成函数调用 形参和实参 位置对应
print_info('小蔡',24,'四川')
# 2:使用关键字参数 格式 key=value key要和形参名一致
print_info(age=18,address='河南',name='大聪明')
# 3:可以混用  位置参数在前  建议 尽量不混用！
print_info("小桐",address='成都',age=19)
# print_info(name="小桐",address='成都',19)# 不行
print_info("小桐",19,address='成都')# 可以

# 定义一个元组传参 --- 本质
tuple1 = ('小松',32,'长春')
# print_info(tuple1)# 直接传递元组 不行 他认为 tuple1 是第一个参数的值 也就是不会自动拆包
# 使用解包语法
print_info(*tuple1) #  * 完成元组的解包

dict1 = {"age":27,"name":"小李","address":"ICU"}
print_info(**dict1) # 字典需要 ** 解包

