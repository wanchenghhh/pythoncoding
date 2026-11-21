"""
  用程序来模拟 超市结账案例
   需求
      买商品 ---输入完成
       商品名字  冰红茶
       商品价格  3.5
       商品数量  70

      小票打印:--输入完成
           您购买了冰红茶,商品单价是3.5元,数量70瓶,总价245元。
"""

name = input('请输入商品的名称:')
price = input('请输入商品的价格:')
count = input('请输入商品的数量:')

# 计算总价
total = float(price) * int(count) # 完成了转换

print(type(total))#<class 'float'>

print(f'购买了{name},商品单价是{price}元,数量{count}瓶,总价{total}元。')
