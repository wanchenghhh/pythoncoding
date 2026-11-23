"""
 字典的遍历
"""
score_dict={
    '李四':90,
    '王五':89,
    '赵六':76,
    '钱七':90,
    '老炮':9
}
#每个键值都展示出来
#  先遍历键 根据键找值
for key in score_dict.keys():
    print(key,score_dict[key])

print("="*100)

for key,value  in  score_dict.items():
     print(key,value)
