# -*- coding: utf-8 -*-
import re

#re模块提供一个方法叫compile模块，提供我们输入一个匹配的规则
#然后返回一个pattern实例，我们根据这个规则去匹配字符串
pattern = re.compile(r'\d+\.\d*')

#通过partten.findall()方法就能够全部匹配到我们得到的字符串
result = pattern.findall("123.141593, 'bigcat', 232312, 3.15")

#findall 以 列表形式 返回全部能匹配的子串给result
for item in result:
    print item