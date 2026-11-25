"""
 缺省参数和不定长参数
"""
"""
   默认参数: 也叫缺省参数,在定义函数的时候，形参有默认值
       作用: 调用的时候不写改参数,参数有默认值，默认值后面不允许有非默认值
   不定长参数:  也叫可变参数  参数的个数可变！
       根据传参的方式分成了
          位置不定长参数  *args 调用的时候,参数位置传参方式，本质是个元组
          关键字不定长参数  **kwargs 调用的时候,关键字位置传参，本质是个字典 
"""

# 定义函数
def print_info(name,age,address='北京'):  # 在声明的时候 给形参了一个默认值
    print(f'姓名:{name},年龄:{age},住址:{address}')

# 调用 默认值函数
print_info('小龙',18)
print_info(age=19,name='小龙')

# 定义一个函数 求多个数据之和
def get_sum(*args): # 本质是元组
    # args的本质是
    # print(type(args))# <class 'tuple'>
    print(sum(args)) #求和
    # for a in args:
    #     print(a)

get_sum(1,2,3)  #  位置参数
get_sum(1,2,3,5,6,6,6,6,6,6,6,1,3,4,4,3,4,43,34,34,34)
get_sum()

def info(**kwargs):# k1=v1,k2=v2,k3=v3 字典格式
    # kwargs 字典
    for k,v in kwargs.items():
        print(k,v)
# 关键字参数
info(name="小晨晨",age=22,address='吉林')

# 函数 可以接收位置参数  也可以接收关键字参数
def fun(*args,**kwargs):
    for a in args:
        print(a)
    for k,v in kwargs.items():
        print(k,v)
    print(f'位置参数传递了{len(args)}个,关键字参数传递了{len(kwargs)}个')


