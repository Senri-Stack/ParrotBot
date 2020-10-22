import random

# command_file = open
# raw_data = command_file.read()
# command_file.close()
# lines = raw_data.splitlines()

with open('miss_dict.txt', encoding='utf-8') as f:
    raw_data = f.read()
    lines = raw_data.splitlines()

miss_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    miss_dict[key] = response

print('ピーチャン>コンニチハ！ ボク、ピーチャン！')
command = input('あなた> ')

num = random.randrange(1, 7)
rand = random.choice(['a','b','c'])

if num >= 6 :
    for message in miss_dict:
        if message in command:
            response = miss_dict[rand]
else:
    response = command

print('ピーチャン>{}'.format(response))
