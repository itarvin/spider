# -*- coding: utf-8 -*-
import re
pattern = re.compile(r'\d+')   # 查找数字

result1 = pattern.findall('hello 123456 789')
result2 = pattern.findall('one1two2three3four4', 0, 10)

print result1
print result2