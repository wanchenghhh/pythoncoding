"""
  open函数 是全局函数
"""
"""
  在python中对文件的玩法 
     打开文件  读写文件  关闭文件 
     打开文件 采用 open函数来完成 
      file文件对象 = open(文件的位置,操作方式)
        文件位置:  文件在系统的路径
          E:\\AIGC\\code\\AI_base_class\\10-文件\\a.txt
           注意写双斜杠 或者反斜杠
        文件路径有三种写法
          1:绝对路径写法  win 盘符开头的  mac/linux  杠开头 
          2:相对路径  相对当前文件的路径！！！
          3:网络路径 (设置图片的路径)   

          注意事项 
             访问当前路径  ./  
             访问上一级   ../

        操作方式 
            读 r   写 w   追加 a  

      关闭文件 
          close()       

"""
# 打开文件
# f = open("E:\\AIGC\\code\\AI_base_class\\10-文件\\a.txt","r")
f = open("a.txt", "r")
print(f)

# 关闭文件
f.close()