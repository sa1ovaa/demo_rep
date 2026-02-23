#1
import re
a = input()
res = re.search(r'ab*',a)
print(res)

#2
import re 
a1 = input()
res1 = re.search(r'ab{2,3}',a1)
print(res1)

#3
import re 
a2 = input()
res2 = re.findall(r'\b[a-z]+_[a-z]+\b',a2)
print(res2)

#4
import re
a3 =input()
res3 = re.findall(r'\b[A-Z]{1}[a-z]+\b',a3)
print(res3)

#5
import re 
a4 = input()
res4 = re.search(r'a.*b$',a4)
print(res4)

#6
import re 
a4 = input()
res5 = re.sub("\s|\,|\.",":",a4)
print(res5)

#7
import re 
a7 = input()
res7 = re.sub("_([a-z]){1}",lambda match: match.group(1).upper(),a7)
print(res7)

#8
import re
a8 = input()
res8 = re.split("(?=[A-Z])",a8)
print(res8)

#9
import re
a9 = input()
res9 = re.sub('(?=[A-Z])',' ',a9)
print(res9)

#10
import re
a10 = input()
res1 = re.sub('([A-Z]){1}',lambda match:"_"+match.group(1).lower(),a10).lstrip('_')
print(res1)