from datetime import datetime
import json
import re


def gather_files(files_arg, suffix=".py"):
    if all([f.endswith(".txt") for f in files_arg]):
        files = []
        for f in files_arg:
            with open(f) as fp:
                for line in fp.readlines():
                    files.append(line.rstrip())
    else:
        for f in files_arg:
            if not f.endswith(suffix):
                raise Exception(f"Incorrect argument, expected {suffix} file: {f}")
        files = files_arg
    return files


def timestamp():
    epoch = datetime.utcfromtimestamp(0)
    now = datetime.now()
    return round((now-epoch).total_seconds()*1000000.0)

def exec_predict(name, e):
    globals_dict = {}
    exec(e, globals_dict)
    return globals_dict[name], e

def store_memory(target, path):
    with open(path, 'w') as f:
        json.dump(target, f)

def load_memory(path):
    with open(path, 'r') as f:
        loaded_dict = json.load(f)
    return loaded_dict

def remove_comments(code):
    # 删除单行注释
    code = re.sub(r'(?<!\\)#.*$', '', code, flags=re.MULTILINE)
    
    # 删除多行注释
    code = re.sub(r'(?s)(?<!\\)""".*?(?<!\\)"""', '', code)
    code = re.sub(r'(?s)(?<!\\)\'\'\'.*?(?<!\\)\'\'\'', '', code)

    return code

def check_import(code):
    globals_dict = {}
    try:
        exec(code, globals_dict)
        return True
    except:
        return False

def remove_indentation(code):
    lines = code.split('\n')  # 将代码按行拆分成列表
    min_indent = float('inf')  # 初始化最小缩进为无穷大

    # 找到最小缩进量
    for line in lines:
        stripped_line = line.lstrip()  # 去掉行首空白字符
        if stripped_line:  # 忽略空白行
            indent = len(line) - len(stripped_line)  # 计算缩进量
            if indent < min_indent:
                min_indent = indent

    # 去除缩进
    if min_indent > 0:
        for i in range(len(lines)):
            lines[i] = lines[i][min_indent:]

    # 拼接代码行并返回
    return '\n'.join(lines)