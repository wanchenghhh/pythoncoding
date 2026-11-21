"""
"""
"""
  死循环
      就是 循环停不下来了！！！
      永真循环！！ 就是 条件永远是True,停不下来

      如果我们 有次数 避免出现死循环！！
      但是如果不知道次数 可以合理的使用 while True 配合 break 使用
"""
"""
    如果我们设置条件,没有设置好,那么就会停不下来。

    使用 while True 优化 猜数字小游戏 
     之前的写法 只能猜一次  一直猜 猜对结束 所以是不知道次数的 
     while True 
     但是 我知道有猜对条件 如果猜对了 就结束循环

"""
import random

# 1:生成一个1-100随机数
guess_num = random.randint(1, 100)  # 随机数

while True:
    # 2:接收用户  录入的整数
    input_num = int(input('请录入您要猜的整数:'))

    # 3:写判断语法
    if input_num == guess_num:
        print('恭喜您猜对了,请找静静老师领取一份5年面试3年笔试大礼包')
        # 猜对了需要 break
        break
    elif input_num > guess_num:
        print('哎呀,您猜大了')
    else:
        print('哎呀,您猜小了')






