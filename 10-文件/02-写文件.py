"""
 完成写文件
   特点 如果文件不存在可以自动创建
   注意
      写中文文件要 设置编码
      模式如果是 w 说明 会先将原来的数据情况 重新书写
      如果想保留原来内容 用追加 a

"""
# 打开文件设置 操作模式为  w
# f = open('python.txt','w',encoding='utf-8')
f = open('python.txt','a',encoding='utf-8') # 追加 在原来的信息后面添加
# 写文件
f.write("\n人民万岁")
# 关闭文件
f.close()