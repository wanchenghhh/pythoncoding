"""

"""
"""
  1:函数定义格式
   def 函数名(形参):
       函数体
       return 返回值
  2:函数调用格式
    完整格式
     变量 = 函数名(实参) 
    如果没有返回结果 就是None,没有必要接收,就直接调用
    如果没有参数需要传递,调用直接()

  3:注意事项 
    函数先定义后调用，不调用不执行。
    函数调用一次就执行一次，每次调用都是独立的。
    函数定义时候()写的就是形参，调用时候写的就是实参。
    函数里面可以写return，可以不写。
    return作用 表示函数结束, 有返回值会把返回的结果赋值给调用者。
    return 可以返回一个结果，可以返回一组结果(自动封装元组)
    没有return的函数，返回的结果None

  4:什么实参 什么是形参  
    函数定义时候()写的就是形参，调用时候写的就是实参。

  5: 函数嵌套调用 
     在一个函数内部 去调用另一个函数 
        当程序调用 b 的时候 函数体遇到了调用a函数,会暂停当前b函数,执行a函数，a函数执行完毕，再继续 
"""


def add(a, b):
    """
    当前函数的说明文档
    两数相加
    :param a: 第一个数
    :param b: 第二个数
    :return: 和
    """
    return a + b


sum = add(1, 2)
print(sum)


def a():
    print("a函数执行了")


def b():
    print("b函数第一句话")
    a()  # 调用a a没执行完 后面的就不执行
    print("b函数最后一句话")


b()
"""
  为什么有函数之间的嵌套调用呢？
    应对模块化开发 
      把大任务 拆成 小任务 
      小任务 可以自由组合 
"""


def brew_coffee():
    return "一杯卡布奇诺"


def fry_egg():
    return "一个太阳蛋"


def toast():
    return "两片吐司"


def douzhi():
    return "一碗隔夜的地道的豆汁"


def make_breakfast():
    print("====开始做早餐=====")
    my_coffee = douzhi()
    my_toast = toast()
    my_egg = fry_egg()
    print(f'今日早餐有:{my_coffee}、{my_toast}、{my_egg}')
    print("====早餐准备完毕=====")
    return my_coffee, my_toast, my_egg


breakfast = make_breakfast()

print(breakfast)