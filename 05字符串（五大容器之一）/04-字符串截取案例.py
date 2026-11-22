"""
     给定一个图片的名称为"avatar.png"，代码实现获取这个图片的名称(avatar)以及这个图片的后缀(.png)。
"""
# 上传的原始文件的名字
image_str = 'avatar.png'
# 获取 点号的 索引
#index = 6 # 先人工数出来 后用方法去完成
index = image_str.rfind('.')# .从右 找到 位置
# 截取文件名称
name = image_str[:index]
print(f'上传的文件名:{name}')
# 截取文件的后缀名
post_fix = image_str[index:]
print(f'上传文件的后缀:{post_fix}')