
from random import seed, random

seed(1)
print(random()) #0.134364244112
print(random()) #0.847433736937

seed(1)
print(random()) #0.134364244112
print(random()) #0.847433736937

from random import seed, random
 print(random()) # 0.885350193339
 print(random()) # 0.381136740351

 print(random()) # 0.634755066626
 print(random()) # 0.130661237179

import string

string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.

from random import choice
import string

tamanho = 5
valores = string.ascii_lowercase
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print(senha)

tamanho = 5
valores = string.ascii_lowercase + string.digits
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print(senha)

valores = string.ascii_letters + string.digits + string.punctuation
