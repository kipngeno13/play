import re

phoneNumRegex = re.compile(r'0\d{9}')
num = phoneNumRegex.search('my number is 0752456171')
print('number found '+num.group())