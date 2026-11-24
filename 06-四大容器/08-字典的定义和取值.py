"""
  字典的定义与取值
"""
"""  
"""
# 定义空字典
dict1 = {}
dict2 = dict()

# 定义非空字典
"""
  特点
    key 是唯一的！！ 出现重复 后面的值覆盖前面的
    key 的类型只能不可变类型 整数 小数 布尔 字符串 元组  
"""
dict3 = {"name":"小晨晨","age":21}
dict4 = {1:"张三",2:"李四",2:"小明"}
print(dict3) # {'name': '小晨晨', 'age': 21}
print(dict4) # {1: '张三', 2: '小明'}


# 取值  字典[key]  如果键不存在就报错
print(f'dict3["name"]:{dict3["name"]}')
# print(f'dict3["username"]:{dict3["username"]}') # KeyError: 'username'
# 取值方式 字典名.get(key) 如果键不存在不报错 返回 None
print(f'dict3.get("name"):{dict3.get("name")}')
print(f'dict3.get("usuername"):{dict3.get("username")}')


# 字典能嵌套 值也可以是字典类型
score_dict = {
    "小王":{"语文":100,"数学":100,"地理":100},
    "小张":{"语文":120,"数学":120,"地理":120},
    "小松":{"语文":150,"数学":150,"地理":150}
}
# 去除 小松的地理成绩
print(score_dict.get('小松').get('地理'))

