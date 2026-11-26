"""
  读取字符文件 文本文件
    readline()
    readlines()
"""
# 1:打开源文件
#src_f = open('论语.txt','r',encoding='utf-8')
with open('论语.txt','r',encoding='utf-8') as src_f:
    # 2:全部读取
    lines = src_f.readlines()
# # 关闭
# src_f.close()

# 3:解析 lines每一行 实现 每行反转 ，存到新的列表中
# 3.1 初始化一个列表
revers_lines = []
# 3.2 遍历 拿到每一行
for line in lines:
    # 解析line   ['子曰：有朋自远方来，不亦乐乎。\n', '子曰：学而不思则罔，思而不学则殆。']
    # 去掉 \n
    strip_line = line.strip("\n") # strip 指定去除的符号
    # 反转
    revers_line = strip_line[::-1]
    # 把反转后的存到 revers_lines 里面
    revers_lines.append(revers_line+"\n")
# 把最后一个元素的换行
revers_lines[-1] = revers_lines[-1].replace("\n","")

# 4:写到新的文件
# 4.1 打开新的文件
#dest_f = open('语论.txt','w',encoding='utf-8')
with open('语论.txt','w',encoding='utf-8') as dest_f:
    dest_f.writelines(revers_lines)
# 关闭
#dest_f.close()