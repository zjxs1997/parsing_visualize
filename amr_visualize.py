import re

split_pattern = '[ (\(\))]'
split_tele = re.compile(split_pattern)


def amr2dag(filepath):
    amr_in = open(filepath, encoding='utf-8')
    amr_lines = []
    for line in amr_in:
        if not line[0] == '#':
            amr_lines.append(line)
    nodes = []
    edges = []
    node_label_dict = {}
    src_node_id = -1
    for line in amr_lines:
        line = line.strip()
        if line[0] == '(':
            sp = 
    # 不是，我记得我应该写过这个代码的。。。
    


