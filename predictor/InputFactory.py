import itertools
import json
import re
import torch as t
from ..Logging import logger
from ..Hyperparams import Hyperparams as params
from ..Util import remove_comments
import ast
# special tokens already provided by the tokenizer
mask_token = "<mask>"
kind_name_token = "<extra_id_2>"
kind_call_token = "<extra_id_3>"
kind_attribute_token = "<extra_id_4>"
sep_token = "<extra_id_5>"
dir = "/"

class ValueInputFactory(object):
    def __init__(self, iids):
        self.iids = iids
        self.file_to_lines = {}

    def _get_lines(self, file_name):
        if file_name in self.file_to_lines:
            return self.file_to_lines[file_name]
        else:
            with open(file_name, "r") as f:
                lines = f.readlines()
            self.file_to_lines[file_name] = lines

            if len(self.file_to_lines) > 10000:  # prevent OOM
                self.file_to_lines = {}

            return lines
    def _get_lvalues(self, code):
        tree = ast.parse(code)

        lvalues = set()

        class LValueVisitor(ast.NodeVisitor):
            def visit_Assign(self, node):
                # 处理赋值语句
                for target in node.targets:
                    self._process_target(target)

            def _process_target(self, target):
                if isinstance(target, ast.Name):
                    lvalues.add(target.id)
                elif isinstance(target, ast.Subscript):
                    # 处理带有下标的情况，例如 a[1]
                    self._process_target(target.value)
                elif isinstance(target, ast.Attribute):
                    # 处理属性的情况，例如 obj.attribute
                    self._process_target(target.value)
                elif isinstance(target, ast.Tuple):
                    # 处理元组解包的情况
                    for element in target.elts:
                        self._process_target(element)

        visitor = LValueVisitor()
        visitor.visit(tree)

        return list(lvalues)
    
    def _check_rvlaue(self, code, target):
        class VariableUsageChecker(ast.NodeVisitor):
            def __init__(self, target_variable):
                self.target_variable = target_variable
                self.used_lines = set()

            def visit_Name(self, node):
                # 处理变量引用
                if node.id == self.target_variable and not isinstance(node.ctx, ast.Store):
                    self.used_lines.add(node.lineno)

        tree = ast.parse(code)
        checker = VariableUsageChecker(target)
        checker.visit(tree)

        return checker.used_lines

    
    def _slice(self, lines, location):
        target_line = lines[location.line-1].strip()
        try:
            if target_line.endswith(":"):
                target_line = target_line+"pass"
            if target_line.endswith("("):
                target_line = target_line+")"
            l_values = self._get_lvalues(target_line)
            code = "\n".join(lines[location.line::])
            for l_value in l_values:
                rvalue_lines = self._check_rvlaue(code, l_value)
                for i in rvalue_lines:
                    target_line += "\n"
                    target_line += lines[i-1].strip()
        except:
            pass
        return target_line
        

    def name_get_input(self, entry, location, lines, env):
        # format of input:

        target_line = self._slice(lines, location)

        # self is hard for llm
        if entry['name'] == 'self':
            entry['name'] = "my_obj"
        
        entry['target_line'] = target_line.replace("self", "my_obj")


        if f"name#{entry['name']}" in env:
            entry['previous'] = env[f"name#{entry['name']}"]

        return entry
    
    def attribute_get_input(self, entry, location, lines, env):

        def get_root_object(code, attr):
            tree = ast.parse(code)

            class TargetPropertyVisitor(ast.NodeVisitor):
                def __init__(self):
                    self.target_node = None

                def visit_Attribute(self, node):
                    # 检查属性名是否为目标属性
                    if node.attr == attr:
                        self.target_node = node

            visitor = TargetPropertyVisitor()
            visitor.visit(tree)
            target_node = visitor.target_node

            if target_node is not None:
                root_object = next(ast.walk(target_node))

                while(hasattr(root_object,'value')):
                    if hasattr(root_object.value, 'attr'):
                        attr = f'{root_object.value.attr}.{attr}'
                    root_object = root_object.value
                root_name = root_object.id
            return root_name, attr


        target_line = self._slice(lines, location)
        root_name,attr = get_root_object(target_line, entry['attr'])
        entry['target_line'] = target_line.replace("self", "my_obj")
        entry['name'] = root_name
        if entry['name'] == 'self':
            entry['name'] = "my_obj"
        entry['attr'] = attr

        if f"name#{entry['name']}" in env:
            entry['previous'] = env[f"name#{entry['name']}"]

        return entry

    def call_get_input(self, entry, location, lines, env):
        # format of input:

        target_line = self._slice(lines, location)

        # self is hard for gpt
        if entry['name'] == 'self':
            entry['name'] = "my_obj"
        
        entry['target_line'] = target_line.replace("self", "my_obj")


        if f"call#{entry['name']}" in env:
            entry['previous'] = env[f"call#{entry['name']}"]

        return entry


    def entry_to_inputs(self, entry, env):
        location = self.iids.location(str(entry["iid"]))

        lines = self._get_lines(dir + location.file+'.orig')

        if entry["kind"] == "name":
            input_dict = self.name_get_input(entry, location, lines, env)

        if entry["kind"] == "attribute":
            input_dict = self.attribute_get_input(entry, location, lines, env)

        if entry["kind"] == "call":
            input_dict = self.call_get_input(entry, location, lines, env)

        return input_dict
    
class TypeInputFactory(object):
    def __init__(self, iids):
        self.iids = iids
        self.file_to_lines = {}

    def _get_lines(self, file_name):
        if file_name in self.file_to_lines:
            return self.file_to_lines[file_name]
        else:
            with open(file_name, "r") as f:
                lines = f.readlines()
            self.file_to_lines[file_name] = lines

            if len(self.file_to_lines) > 10000:  # prevent OOM
                self.file_to_lines = {}

            return lines


    def entry_to_inputs(self, entry):
        location = self.iids.location(str(entry["iid"]))

        lines = self._get_lines(dir + location.file+'.orig')
        
        entry['target_line'] = lines[location.line-1]

        return entry
