"""
- 使用 input() 输入两个整数 a 和 b
- 使用 if-elif-else- 结构输出较大的那个数
- 如果相等，输出“两数相等”
"""
# 输入两个整数
a = int(input('请输入一个整数:'))
b = int(input('请输入另一个整数:'))

# 找出较大的数  如果相等就输出相等
# if a > b :
#     print(f'a是较大值:{a}')
# elif a < b :
#     print(f'b是较大值:{b}')
# else:
#     print(f'a和b的值相等,都是{a}')

#  if-else ？
if a == b:
    print(f'a和b的值相等,都是{a}')
else:
    if a > b:
        print(f'a是较大值:{a}')
    else:
        print(f'b是较大值:{b}')

"""
  什么是if嵌套呢？
    就是 在if语句中  子语句 里面依然出现了if结构  这就是if嵌套

  比如说 
     退休年龄  什么时候退休 
     if 是男:
       if 年龄==63:
          可以领退休金

     else:   
       if 年龄==60:
          可以领退休金

"""