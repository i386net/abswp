import re

nums_regex = re.compile(r'^(\d{1,3})((,\d{3})*)$', re.MULTILINE)
text = '''
000,123,234
23,344,123
123456
2,56,777
42'''

nums = nums_regex.findall(text)
#print(nums)
for n in nums:
    print(n[0] + n[1])
