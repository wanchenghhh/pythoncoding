"""
 match case
"""
"""
  match case
     也是一种分支语句  是python10之后的语法 
     主要是对值 进行匹配 

     match 待匹配的变量:
        case 值1:  # 匹配单个的值
          语句1
        case 值2:  # 匹配单个值 
          语句2
        case 值3|值4|值5:  #匹配多个值
          语句3
        case 变量名 if 条件:  # 对变量进行判断  s if s>95 
          语句4
        case _: # 默认语句
          语句5          
"""
# 输入月份 告诉我季节
month = int(input('请输入月份:'))

match month:
    case 3 | 4 | 5:
        print(f'当前{month},是春天！')
    case 6 | 7 | 8:
        print(f'当前{month},是夏天！')
    case 9 | 10 | 11:
        print(f'当前{month},是秋天！')
    case 12 | 1 | 2:
        print(f'当前{month},是冬天！')
    case _:
        print(f'当前值{month}不是月份')

# 输入分数 返回一个等级 不直接打印 使用变量接收等级
score = int(input('请输入分数:'))

match score:
    case s if s >= 90:  # s是临时变量 用来接收 score  if 对 接收的变量进行判断  匹配就执行子语句
        grade = "A"
    case s if s >= 75:
        grade = "B"
    case s if s >= 60:
        grade = "C"
    case _:
        grade = "D"
print(f'成绩{score}的等级是{grade}')
