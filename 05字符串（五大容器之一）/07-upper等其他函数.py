"""
  玩一玩字符串的其他方法
     玩一玩就行
"""
#  upper() / lower()：全部转为大写/小写。
name = "jackMa"
print(name.upper())# JACKMA
print(name.lower())# jackma
print(name.title())# Jackma

#   isalpha() 判断是否是全字母
print(name.isalpha()) # True
print(name.isdigit()) # False
print("123一".isdecimal())
print("123一".isnumeric())

