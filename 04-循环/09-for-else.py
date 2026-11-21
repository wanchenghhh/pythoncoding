
"""
"""
"""
 小知识
   循环可以和else配合使用  else 下发的代码标识 循环正常结束后 执行
   
   for ....:
      循环体
   else:
     表示for循环正常的结束
=========================================

break 终止循环，为非正常结束，不执行else语句
continue 中断本次循环，继续下一次循环。为正常结束，执行else语句。

"""

str1 = "ikunji"
# 发现 j 就不打印了
for a in str1:  # a 取值  i  k  u  n  j
    if a == "j":
        break # 非正常结束
    print(a)
else:
    print("循环正常结束后执行....")

for a in str1:  # a 取值  i  k  u  n  j  i
    if a == "j": # 跳过j 打印 不打印j 打印后面的
        continue # 正常结束
    print(a)
else:
    print("循环正常结束后执行....")

