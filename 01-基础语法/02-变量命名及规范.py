""""""
"""
  什么是变量呢？
     变量就是内存中的一小块区域，用来存储数据的
     特点 在程序运行时可以发生改变，是临时的，因为程序停止，变量消失。
  变量定义格式:
    变量名 = 数据值     
"""
# 定义一个变量
name = 'the shy'
age  = 28
height =18.3
stuid= 23455

# 怎么访问  直接打印 变量名
print(name)
print(age)
print(name,age)

"""
  这小节两个知识点
    变量的命名规范(有认知)
    变量的数据类型(掌握)
"""
"""
  变量的命名规范---标识符的规则
      标识符！！用来标识的符号！！比如 你的名字用来标识 你本人！！
  不能太随意，有一定的规则和规范 
    强制要求--必须遵守的
       ① 由数字字母下划线组成  
       ② 数字不能开头
       ③ 严格区分大小写
       ④ 不能使用关键字作为变量名    
    软性建议--建议遵守的
       变量名字定义的时候 
          一般都是小写字母组成 
          如果有多个单词组成 我们类名 采用小驼峰  首个单词小写第二个单词开始首字母大写
                         变量建议 是 下划线命名法
"""
"""
  常见的七种数据类型  
    数值型  整数 int  小数 float 
    布尔型  True 真 Fasle 假
    容器类型  字符串 string 
             列表 list
             元组 tuple
             集合 set 
             字典 dict
"""
"""
  可以直接使用的函数：type() isinstance()            
    1,type(数据/变量) 返回的 数据的类型 
    因为它不会自己打印，所以我们使用print( type(...) ) 
    
    2,isinstance(age,str) 判断数据的类型是否正确
    因为它不会自己打印，所以我们使用print( isinstance(...) )       
"""
# 定义一个人
name = '徐坤·菜'
age = 32
height = 1.85
sex = True

# 查看数据类型  type(数据/变量) 返回的 数据的类型
print(name,type(name)) # 徐坤·菜 <class 'str'>
print(age,type(age))  # 32 <class 'int'>
print(height,type(height))# 1.85 <class 'float'>
print(sex,type(sex)) # True <class 'bool'>

# 判断 isinstance(数据/变量,类型) 判断你的数据是不是这个类型
print(isinstance(name,str)) # True
print(isinstance(age,str))   #False



