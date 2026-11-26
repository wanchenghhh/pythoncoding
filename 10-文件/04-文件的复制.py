"""
 完成文件的复制
   ../蛋糕.JPG
   什么是文件复制？  把蛋糕.JPG所有字节数据 拷贝出来 存到另一个位置
   蛋糕.JPG 源文件    生日.JPG 目标文件
   通过程序 把 蛋糕.JPG 里面 所有的字节 写到 生日.JPG里面

"""
"""
  适合小文件复制
# 1:打开 蛋糕.JPG 操作模式 rb
src_f = open('../蛋糕.JPG','rb')
# 2: 从 源文件中读取出数据 数据读取到内存中
content = src_f.read() # 直接读取到内存
# 3: 打开 生日.JPG 操作 wb
dest_f = open('../生日.JPG','wb')
# 4: 将刚才读到内存中的数据 写入到 目的地中
dest_f.write(content)
# 5: 关闭文件
src_f.close()
dest_f.close()  

大文件 
"""
# 1:打开 蛋糕.JPG 操作模式 rb
src_f = open('../蛋糕.JPG','rb')
# 2: 打开 生日.JPG 操作 wb
dest_f = open('../生日2.JPG','wb')
# 3: 边读  边写
while True:
    content = src_f.read(1024) # 每次读取 1KB
    if len(content) <= 0: # 按数量
        break
    # 写到文件中
    dest_f.write(content)
# 4: 关闭文件
src_f.close()
dest_f.close()
