import os
from datetime import date
## init해 놓은 폴더로 이동
os.chdir('git 폴더')

print(os.path)
output = os.popen('git init').read()
print(output)
output = os.popen('git add .').read()
print(output)
output = os.popen("git commit -m 'auto{}'".format(date.today())).read()
print(output)
output = os.popen('git push origin main').read()
print(output)