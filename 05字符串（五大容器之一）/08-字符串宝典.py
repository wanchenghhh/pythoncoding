"""
  字符串常用功能
"""
"""
1. 大小写与格式转换
    upper() / lower()：全部转为大写/小写。

    capitalize()：首字母大写，其余小写。

    title()：每个单词首字母大写。

    swapcase()：大小写互换。

    casefold()：更激进的小写转换（用于无差别比较，如德语 ß 转 ss，比 lower() 更强）。

2. 判断类型（返回布尔值）
    isalpha()：是否全是字母。

    isdigit() / isnumeric() / isdecimal()：是否全是数字（中文数字 "三" 只能用 isnumeric() 识别）。

    isalnum()：是否全是字母或数字。

    isspace()：是否全是空白字符（空格、换行、制表符）。" " "\n" "\t"     

    islower() / isupper() / istitle()：是否全小写、全大写、符合标题格式。

    startswith(prefix) / endswith(suffix)：是否以某字符串开头/结尾（支持元组参数）。

3. 查找与定位
    find(sub) / rfind(sub)：从左/从右查找子串首次出现的索引，找不到返回 -1。

    index(sub) / rindex(sub)：功能同上，找不到抛出 ValueError 异常。

    count(sub)：统计子串出现的非重叠次数。

4. 拆分、合并与分割
    split(sep)：按分隔符切分为列表（默认按任意空白切分）。

    rsplit(sep)：从右侧开始切分。

    splitlines()：按换行符切分，保留换行符可选。

    partition(sep) / rpartition(sep)：将字符串切为 (头, 分隔符, 尾) 三元组。

    join(iterable)：将可迭代对象（如列表）用当前字符串连接起来（高频常用）。

5. 去除空白与指定字符
    strip() / lstrip() / rstrip()：去除两端/左侧/右侧的空白字符（可指定要去除的字符集）。

6. 替换与翻译
    replace(old, new, count)：替换子串（可指定替换次数）。

    translate(table) 配合 str.maketrans()：按映射表批量替换单个字符（比 replace 效率高，适合密码表映射）。

7. 填充、对齐与补零
    center(width, fillchar)：居中对齐填充。

    ljust() / rjust()：左对齐/右对齐填充。

    zfill(width)：右侧对齐，左侧用 0 填充（常用于数字补零，如 "42".zfill(5) => "00042"）。

8. 格式化字符串
    format(*args, **kwargs)：强大的格式化方法，如 "{} is {}".format("A", 1)。

    （注：现代 Python 更推荐 f-string，如 f"{name}"，它不属于函数，而是语法糖）。



"""