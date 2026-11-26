"""
  读文件
"""
"""
一般文件分成两大类
   可以使用记事本打开的这种文本文件 --- 字符文件 .py .java .h .md .html .txt 
        这些文件里面都是 字符串(文本)内容
   用记事本打开出现乱码的  -- 字节文件  .mp4 .avi .mp3 .word .pdf ...
        这些文件不是由文本组成的, 这些文件底层都是二进制文件！！ 叫 字节(二进制)文件

   针对 文本文件的操作模式 
       r  w  a  
   针对 字节文件    b 是二进制的缩写
       rb wb ab               

   文本文件有编码  字节  <----编码表-----> 字符
   读写文本文件时 必须加上 encoding='utf-8'  现在开发都采用 utf-8编码 
   读写字节文件时 不需要 它里面只有字节！！

   读的方法  

   针对所有文件:
      read() 读取文件全部内容 --适合小文件
      read(size)  根据size的长度读取文件的数据(字节/字符) 
         size 个数  字节文件--字节个数  字符文件--字符个数
   针对文本文件
      readline() 按照一行行读取,读完这一行,就会自动到下一行
      readlines() 对文件整体的读取,自动完成切割,切割成若干行,每一行存到到一个列表中。        

   注意事项 
     读取文件,要求文件必须存在！！！否则 报错 FileNotFoundError

"""
f1 = open('静夜思.txt', 'r', encoding='utf-8')
# 使用read()读
content1 = f1.read()
print(content1)
f1.close()
print("====================================================")
f2 = open('静夜思.txt', 'r', encoding='utf-8')
# 使用read(size)读
content2 = f2.read(5)
print(content2)
f2.close()
print(
    "=================readline() 按照一行行读取,读完这一行,就会自动到下一行  大文件===================================")
f3 = open('静夜思.txt', 'r', encoding='utf-8')
# readline()  会把换行读取出来
# line1 = f3.readline()
# line2 = f3.readline()
# print(line1,end="")
# print(line2,end="")
# readline配合循环使用
while True:
    line = f3.readline()
    # 读到末尾 没有内容
    if not line:  # line里面没有内容
        break
    print(line, end="")
f3.close()
print()
print("====readlines() 对文件整体的读取,自动完成切割,切割成若干行,每一行存到到一个列表中。=== ")
f4 = open('静夜思.txt', 'r', encoding='utf-8')
# readlines
lines = f4.readlines()
print(type(lines))
print(lines)
f4.close()