"""
  if ... elif...else 格式
"""
"""
  想表达多种分支，多种情况 就要使用
   if...elif...else格式 格式如下:

   if 条件1:
      语句1
   elif 条件2:
      语句2
   elif 条件3:
      语句3
   ...
   else 
      语句n+1

   执行流程 
     先执行条件1  条件1真  执行语句1,if语句结束
                 条件1假  -- 执行条件2  真  执行语句2 if语句结束 
                                  假  执行条件3  真 执行语句3  if语句结束
                                               假 ....
                                                   ....如果前面所有的条件结果都是false 
                                                       执行 语句n+1            
"""

#  根据录入的成绩  输出它的所属等级
# 输入一个成绩
score = int(input('请录入您的成绩:'))
# score  100-90 优秀   90-80 良好  80-60 及格 60以下 不及格 其他 非法数据
if 90 <= score <= 100:
    print('优秀')
elif 80 <= score < 90:
    print('良好')
elif 60 <= score < 80:
    print('及格')
elif 0 <= score < 60:
    print('不及格')
else:
    print('非法数据')

'''
#上面这个例子，print多次打印
可以用result这个变量接收，最后print({result})即可
'''
