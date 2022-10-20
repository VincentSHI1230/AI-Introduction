py_file = open('./eightpuzzle.py', 'r', encoding='utf-8')
output_file = open('./op.txt', 'w', encoding='utf-8')
op_list = []
r = ''
for line in py_file:
    line = line.strip()
    if line.startswith('#'):
        op_list.append(line)
    for i in line:
        if i in '()':
            r += i