
import re
a='ab_a'
new_s = re.sub(r'[^A-Za-z0-9А-Яа-яЁё]', '', a).lower()
print(new_s)
if new_s[::-1]==new_s[::]:
    print('yes')
else:
    print('net')
