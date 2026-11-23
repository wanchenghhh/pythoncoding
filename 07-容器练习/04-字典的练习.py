"""
 字典练习
"""
"""
  字符串转字典
    给定一个字符串my_string，现在要求统计每个字符出现的次数: 形成结果: {'字符':出现次数,'字符2':次数}
    例如: 'abceacf' ==> {'a':2,'b':1,'c':2,'e':1,'f':1}
"""
# 准备字符串
text = 'abceacf'
# 准备一个记录 字符 及其 出现次数的字典
char_count = {}  #  键 是字符  值 出现的次数

# 遍历 text 字符串 拿到每个字符
# for char  in text:
#     # 判断 ch 有没有在在 字典中出现过
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
for char in text:
    char_count[char] = text.count(char) # 查看字符在字符串出现的次数
# 打印结果
print(char_count)

"""
   需求: 编写一个程序将字符串转换为字典 
   例如:输入: '5=Fi=ve 6=Six 7=Seven'   
   输出: {'5': 'Five', '6': 'Six', '7': 'Seven'}
"""
#  切分 字符串
s =  '5=Five 6=Six 7=Seven'

item_list = s.split(" ")
# 创建字典
result = {}
for item in item_list:
    key,value = item.split("=",1)# 拆包区解析 列表数据 [5,Five]
    result[key] = value

print(result)
