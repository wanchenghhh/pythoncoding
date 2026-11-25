"""
  lambda介绍
"""
"""
   python中大多数的函数都是 有名字的函数  --- 普通函数
       有时候为了简化代码,就不再给函数起名字--匿名函数--lambda函数

   lambda使用前提:
       如果一个函数有一个返回值,并且只有一句代码,就可以使用lambda简化   
     基本语法
       匿名函数的名 = lambda 函数的参数:函数的返回    
       怎么使用
         匿名函数(传递参数) 
"""


def get_pai():  # get_pai 是函数的名字
    return 3.14  # 函数的返回值 (做的事情)


pai = get_pai()
print(pai)
# lambda 的写法 lambda 可以替代函数
#  lambda 参数:以前return后面的内容
p = lambda: 3.14  # 可以理解 右边部分是一个函数简化形式 左边的p 匿名函数的名字
print(p())  # 加()  调用


def add(a, b):  # add 函数的名字 a,b 函数的参数--输入
    return a + b  # 函数的返回值(做的事情)  输出结果


# 改造成 lambda形式
sum = lambda a, b: a + b
# 调用
print(sum(1, 3))

# 求三个数的和
add3 = lambda a, b, c: a + b + c
print(add3(9, 2, 3))


# 普通函数
def is_num(num):
    if num > 0:
        return True
    else:
        return False


# 针对   这种if的处理怎么办？ 先转换成三目 再处理
def is_num2(num):
    return True if num > 0 else False


flag = lambda num: True if num > 0 else False
print(flag(10))

