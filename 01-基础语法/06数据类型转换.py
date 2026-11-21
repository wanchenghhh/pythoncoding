"""
  目标 学会类型的转换
     int(x) 将数据变成整数   有前提 要么字符串是整数字符串 要么小数 只有整数位小数位是0 否则报错
     float(x) 将数据变成小数 有前提 字符串里面的数据需要是数字！！
     str(x) 将数据变成字符串  啥都行！！！
"""
# 演示
a='10'  # str
b='3.14' # str
c= 20   # int
d='cba' # str

# 将a(的数据) 转换成 int 类型
a_int = int(a)
print(a_int,type(a_int)) # 10 <class 'int'>

# 将b的数据 转换 float类型
b_float = float(b)
print(b_float,type(b_float))  # 3.14 <class 'float'>

#  c的数据 转换成 float 类型
c_float = float(c)
print(c_float,type(c_float)) # 20.0 <class 'float'>

# b的数据 3.14 转换 int类型
b_int = int(3.0)# b 不行 3.0可以
print(b_int,type(b_int))  # 3 <class 'int'>

# d_int = int(d)
# print(d_int,type(d_int))

b_str = str(b)
print(b_str,type(b_str)) # 3.14 <class 'str'>

