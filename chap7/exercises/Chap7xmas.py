import re

xmas_regex = re.compile(r'\d+\s\w+')
xm = xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies')
print(xm) 