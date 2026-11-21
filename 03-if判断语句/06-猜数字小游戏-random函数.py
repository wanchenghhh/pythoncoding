"""
 实现猜数字小游戏
"""
"""
   随机产生一个 1-100的随机数 
   让用户猜！！
   判断 用户猜对了  提醒 猜对了
       猜大了     提醒 猜大了 
       猜小了     提醒 猜小了
   实现步骤:
     1:准备随机数？ 产生随机数？ 
        --谁会做就找谁！！ random模块！引入random模块
     2:使用输入函数来完成 input('请输入一个整数来猜一猜随机数是几？')
     3: 做判断 -- 三种情况 
        用 if...elif...else...
 补充知识点  随机数产生 
    ① 导包 引入random模块    import random
    ② 模块里面有个函数 random.randint(a,b) 左闭右闭 范围[a,b]     取值范围包括a,b和a,b之间的整数
    ③ 函数调用完毕 得到一个结果 是int类型 整数     
"""
import random

# 1:生成一个1-100随机数
guess_num = random.randint(1,100)  # 随机数

# 2:接收用户  录入的整数
input_num = int(input('请录入您要猜的整数:'))

#3:写判断语法
if input_num == guess_num:
    print('恭喜您猜对了,请找静静老师领取一份5年面试3年笔试大礼包')
elif input_num > guess_num:
    print('哎呀,您猜大了')
else:
    print('哎呀,您猜小了')