import time
import string
import random

f = open('/root/pyfile/a.txt', 'w')
for i in range(100):
    words = ''.join(random.sample(string.ascii_lowercase, 5))
    row = '--- No.{}, {} ---\n'.format(i, words)
    f.write(row)
    f.flush()
    time.sleep(2)

f.close()
