import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '123456789'
symbols = '!@#$%^&*()_+{}[]:"\'\'<>.,/?'
length_of_password = 15
password = lower_case + upper_case + numbers + symbols
ok = random.sample(password, password)
print(ok)
