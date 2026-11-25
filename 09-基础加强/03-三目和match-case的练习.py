# 1:用三目运算符判断一个数 n 是奇数还是偶数，输出 "奇数" 或 "偶数"。
n = 7
print('奇数' if n%2==1 else '偶数')
print('奇数') if n % 2 == 1 else print('偶数')
# 2: 给定两个数 a, b，用一行三目运算符求出较大值。
a,b = 23,45
print( a if a>b else b)
# 3 用列表推导式 + 三目，把 [1,2,3,4,5,6] 中的偶数变成 0，奇数保持不变。
# 期望结果：[1, 0, 3, 0, 5, 0]
nums = [1,2,3,4,5,6]
list1 = [ 0 if i%2==0 else i for i in nums]
print(list1)
# 4 :把 [3, -1, 0, 7, -5] 中的负数替换成 "负"，非负数替换成 "非负"。
# 期望结果：['非负', '负', '非负', '非负', '负']
nums2 = [3, -1, 0, 7, -5]
list2 = ['非负' if n>=0 else '负' for n in nums2 ]

# 5:从 [-2, -1, 0, 1, 2, 3] 生成一个集合，正数存本身，非正数存绝对值。
# 期望结果：{0, 1, 2, 3}（集合去重）  提示:abs(X) 求X绝对值
nums3 = [-2, -1, 0, 1, 2, 3]
set3 = { abs(n) for n in nums3 }
print(set3)

#6 根据星期数字 1~7 输出：1~5 → "工作日"   6、7 → "周末"  其他 → `"非法"
day = 6
match day:
    case 1|2|3|4|5:
        print('工作日')
    case 6|7:
        print('周末')
    case _:
        print('非法')


"""
7 传入一个变量  输出它的类型描述  。
      输入	输出
     True	"真"
     False	"假"
     None	"空值"
     其他	"其他"
"""
value = None
match value:
    case True:
        print('真')
    case False:
        print('假')
    case None:
        print('空值')
    case _:
        print('其他')

"""
8 题目背景
根据人的身高（米）和体重（公斤）计算 BMI，并按中国标准划分等级：

BMI=体重/身高*身高
BMI 范围	等级
< 18.5	偏瘦
18.5 ~ 23.9	正常
24.0 ~ 27.9	偏胖
28.0 ~ 31.9	肥胖
≥ 32.0	重度肥胖
身高 ≤ 0 或体重 ≤ 0	数据非法
"""
height = 1.75
weight = 70

# 使用match case 来完成
level = ''
if height<=0 or weight<=0:
    print("数据非法")
else:
    bmi = weight / height ** 2
    match bmi:
        case b if b<=18.5:
           level='偏瘦'
        case b if b<=23.9:
           level='正常'
        case b if b<=27.9:
           level='偏胖'
        case b if b<=31.9:
           level='肥胖'
        case _:
            print('重度肥胖')
print(f"身高{height},体重:{weight},bmi:{bmi:.2f},level:{level}")

