"""
"""
"""
    列表的遍历
     第一种方式  推荐方式
          for 临时变量 in 列表:
     第二种方式 while方式 -- 根据索引找元素
"""
#  完成列表的遍历
name_list = ["刘德华","黎明","张学友","郭富城"]
# for遍历方式
for name in name_list:
    print(name, end=" ")
print()

# while 遍历 通过索引找数据
i = 0  # 定义计数器  索引
while i < len(name_list):
    print(name_list[i])
    i += 1  # 更新计数器


# 二维列表  列表嵌套
diqu=[['西安市','渭南市','咸阳市','宝鸡市'],['邯郸','邢台','石家庄','衡水']]
#  根据 diqu 获取到每一个城市
# 先完成第一层遍历  再完成第二层遍历
for diqu_list in diqu:
    # 得到 diqu_list diqu里面的两个列表
    for city in diqu_list:
        print(city, end=" ")
    print()