"""
给定列表 original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]，编写程序对列表中的数据进行去重。
要求：
    - 使用 for 循环遍历原始列表
    - 如果元素不在去重后的列表中，则添加
    - 输出去重后的列表
"""
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# 1 新建一个列表
new_list = []
# 2 遍历 原始的列表
for item in original_list:
    if item not in new_list: # 元素不在新的列表中 就存储
        new_list.append(item)
# 3：打印结果
print(f'去重后的结果:{new_list}')

print("="*100)

# 原始列表
my_list = ["spring", "smail", "look", "strange", "curious","smail", "black", "hope"]
my_list_copy = my_list[:]  # 创建一份新的列表
# 最终列表（期望输出）
# my_list = ['joker', 'hope', 'curious', 'black', 'hope']
# for item in my_list[:]:  # 遍历的是新的列表 遍历目的  保证可以遍历到每一个元素
#     if item.startswith("s"): # 每一个元素 进行判断
#         my_list.remove(item) #  原始中删除
# 倒着删
i = len(my_list)-1
# while循环  i 每个元素的索引  i 从最后一个索引开始
while i>=0:
    item = my_list[i]  #  取出元素
    if item.startswith("s"):
        my_list.remove(item)
    i = i-1


print(my_list)



