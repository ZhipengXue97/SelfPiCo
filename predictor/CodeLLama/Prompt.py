def GetPrompt(entry):
    conversation = []
    if entry["type"] == "value":
        systemrole = """I want you to act like a Python programmer. I will give you Python code and comments, \
            you should write python code according to the comments step by step. \
            Only give reply with completed code and Do not write explanations.\
            Your reply limited into only one code blocks and should wrap with triple backticks."""
        conversation.append({"role":"system", "content":systemrole})
        exampe1 = \
"""
#Task: Complete and fix the given code to make it can be executed directly.
#Given Code:Do not modify the given python code or wrap it with function
#<ctx = _cv_app.get(None)>

#Previous wrong answer, becaues<>

#Step1: import needed module here.

#Step2: Define all the needed class, method or variable here in detail.

#Step3: Define and assign <name><_cv_app>, to repair the error<NameError: name '_cv_app' is not defined>

#Overall, complement code are:
# Do not output Given Code and wrong answer
"""
        result1 = \
"""
#Step1: import needed module here.
# No needed module

#Step2: Define all the needed class, method or variable here in detail.
#Define the class of _cv_app, which includes the function get.
class CVApp:
    def get(self,*args):
        return 0

#Step3: Define and assign <name><_cv_app>, to repair the error<NameError: name '_cv_app' is not defined>
#instant the object _cv_app
_cv_app = CVApp()

#Overall, complement code are:
# Do not output Given Code and wrong answer
class CVApp:
    def get(self,*args):
        return 0
_cv_app = CVApp()
"""
        exampe2 = \
"""
#Task: Complete and fix the given code to make it can be executed directly.
#Given Code:Do not modify the given python code or wrap it with function
#<height, wight = getinfo("Jack")>

#Previous wrong answer, becaues<NameError: name 'AllInfo' is not defined>
def getinfo(name):
    return AllInfo[name][0], AllInfo[name][1]

#Step1: import needed module here.


#Step2: Define all the needed class, method or variable here in detail.


#Step3: Define and assign <call><getinfo>, to repair the error<NameError: name 'getinfo' is not defined>

#Overall, complement code are:
# Do not output Given Code and wrong answer
"""
        result2 = \
"""
#Step1: import needed module here.
# No needed module

#Step2: Define all the needed class, method or variable here in detail.
#Define the AllInfo which will be used in the getinfo function.
AllInfo = {"Jack":(172, 75), "Mary":(165, 50)}

#Step3: Define and assign <call><getinfo>, to repair the error<NameError: name 'getinfo' is not defined>
#Define the getinfo function which will return two value
def getinfo(name):
    return AllInfo[name][0], AllInfo[name][1]

#Overall, complement code are:
# Do not output Given Code and wrong answer
AllInfo = {"Jack":(172, 75)}
def getinfo(name):
    return AllInfo[name][0], AllInfo[name][1]
"""
        exampe3 = \
"""
#Task: Complete and fix the given code to make it can be executed directly.
#Given Code:Do not modify the given python code or wrap it with function
#<filepath = myobj.path>

#Previous wrong answer, becaues<NameError: name 'os' is not defined>
class MyClass(): pass
    self = MyClass()
self.path = os.path.abspath(__file__)

#Step1: import needed module here.

#Step2: Define all the needed class, method or variable here in detail. \

#Step3: Define and assign <attribute><path>, to repair the error<AttributeError: 'myobj' object has no attribute 'path'>

#Overall, complement code are:
# Do not output Given Code and wrong answer
"""
        result3 = \
"""
#Step1: import needed module here.
#import path related module os
import os

#Step2: Define all the needed class, method or variable here in detail. \
#Define the class of myonj and instant myobj
class MyClass(): pass
myobj = MyClass()

#Step3: Define and assign <attribute><path>, to repair the error<AttributeError: 'myobj' object has no attribute 'path'>
#Define the attribute path of myobj
myobj.path = os.path.abspath(__file__)

#Overall, complement code are:
# Do not output Given Code
import os
class MyClass(): pass
    self = MyClass()
myobj.path = os.path.abspath(__file__)
"""
        exampe4 = \
"""
#Task: Complete and fix the given code to make it can be executed directly.
#Given Code:Do not modify the given python code or wrap it with function
#<data = toml.load(file)>

#Previous wrong answer, becaues<ModuleNotFoundError: No module named 'toml'>
#import toml

#Step1: import needed module here.

#Step2: Define all the needed class, method or variable here in detail. \

#Step3: Define and assign <attribute><path>, to repair the error<NameError: name 'toml' is not defined>

#Overall, complement code are:
# Do not output Given Code and wrong answer
"""
        result4 = \
"""
#Step1: import needed module here.
# Do not import toml since No module named 'toml'

#Step2: Define all the needed class, method or variable here in detail. \
#Define the class of Toml
class Toml:
def load(self, file_path):
    with open(self.file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=')
                self._set_nested_value(key.strip(), value.strip())

#Step3: Define and assign <attribute><path>, to repair the error<NameError: name 'toml' is not defined>
#instant toml
toml = Toml()

#Overall, complement code are:
# Do not output Given Code and wrong answer
class Toml:
    def load(self, file_path):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    self._set_nested_value(key.strip(), value.strip())
toml = Toml()

"""
        question =  \
f"""
#Task: Complete and fix the given code to make it can be executed directly.
#Given Code:Do not modify the given python code or wrap it with function
#<{entry['target_line']}>

#Previous wrong answer, becaues<{entry['execute_error']}>
#{entry['wrong_answer']}

#Step1: import needed module here.

#Step2: Define all the needed class, method or variable here in detail. \

#Step3: Define and assign <{entry['kind']}><{entry['name']}>, to repair the error<{entry['orig_error']}>

#Overall, complement code are:
# Do not output Given Code and wrong answer
"""
        # print(question)
        conversation.append({"role":"user", "content":exampe1})
        conversation.append({"role":"assistant", "content":result1})
        conversation.append({"role":"user", "content":exampe2})
        conversation.append({"role":"assistant", "content":result2})
        conversation.append({"role":"user", "content":exampe3})
        conversation.append({"role":"assistant", "content":result3})
        conversation.append({"role":"user", "content":exampe4})
        conversation.append({"role":"assistant", "content":result4})
        conversation.append({"role":"user", "content":question})








    if entry["type"] == "type":
        #few shot
        systemrole = f"""I want you to act as a classifier. I will give you a python code and a \
    <word> in the code. You will classifiy the <word> into catogaries based on its type: \
    None, Boolean, Integer, Float, String, List, Tuple, Set, Dictionary, Tensor, Array, DataFrame, Callable, Resource, Object.\
    I want you to reply with the only one word of classified catogary and nothing else. Do not explain the result.
    """
        conversation.append({"role":"system", "content":systemrole})
        conversation.append({"role":"user", "content":"word: <name> <df>, code: <grouped = df.groupby('A')>"})
        conversation.append({"role":"assistant", "content":"Dataframe"})
        conversation.append({"role":"user", "content":"word: <attribute> <leaves>, code: <start = line.leaves[index]>"})
        conversation.append({"role":"assistant", "content":"List"})
        conversation.append({"role":"user", "content":"word: <name> <index>, code: <start = line.leaves[index]>"})
        conversation.append({"role":"assistant", "content":"Integer"})
        conversation.append({"role":"user", "content":"word: <attribute> <STRING>, code: <if LL[0].type != token.STRING:>"})
        conversation.append({"role":"assistant", "content":"String"})
        conversation.append({"role":"user", "content":"word: <attribute> <parent>, code: <parent = LL[0].parent>"})
        conversation.append({"role":"assistant", "content":"Object"})
        conversation.append({"role":"user", "content":"word: <name> <node>, code: <if not node:>"})
        conversation.append({"role":"assistant", "content":"None"})
        conversation.append({"role":"user", "content":"word: <name> <City>, code: <print(City._fields)>"})
        conversation.append({"role":"assistant", "content":"Tuple"})
        conversation.append({"role":"user", "content":"word: <name> <option_context>, code: <with option_context():>"})
        conversation.append({"role":"assistant", "content":"Resource"})
        conversation.append({"role":"user", "content":"word: <attribute> <format>, code: <exit(self.columns.format())>"})
        conversation.append({"role":"assistant", "content":"Callable"})
        conversation.append({"role":"user", "content":"word: <name> <conditionX>, code: <exit(if conditionX:)>"})
        conversation.append({"role":"assistant", "content":"Boolean"})
        conversation.append({"role":"user", "content":"word: <name> <dict1>, code: <result = dict(Counter(dict1) + Counter(dict2))>"})
        conversation.append({"role":"assistant", "content":"Dictionary"})
        word = f"<{entry['kind']}><{entry['name']}>, code: <{entry['target_line']}>"  
        conversation.append({"role":"user", "content":word})
    return conversation
    

def get_clean_conversation(entry, code):
    conversation = []
    exampe1 = \
"""
#based on the code:
class CVApp:
    def get(self,*args):
        return 0

_cv_app = CVApp()

class CVApp:
    def get(self,*args):
        return 0
_cv_app = CVApp()
ctx = _cv_app.get(None)
The define code of _cv_app is:
```
```
"""
    result1 = \
"""
The define code of _cv_app is:
```
class CVApp:
    def get(self,*args):
        return 0
_cv_app = CVApp()
```
"""
    exampe2 = \
"""
#based on the code:

AllInfo = {"Jack":(172, 75), "Mary":(165, 50)}

def getinfo(name):
    return AllInfo[name][0], AllInfo[name][1]

AllInfo = {"Jack":(172, 75)}
def getinfo(name):
    return AllInfo[name][0], AllInfo[name][1]
height, wight = getinfo("Jack")
The define code of getinfo is:
```
```
"""
    result2 = \
"""
The define code of getinfo is:
```
AllInfo = {"Jack":(172, 75)}
def getinfo(name):
    return AllInfo[name][0], AllInfo[name][1]
```
"""
    exampe3 = \
"""
#based on the code:

class MyClass(): pass
    self = MyClass()
self.path = os.path.abspath(__file__)

import os

class MyClass(): pass
myobj = MyClass()

myobj.path = os.path.abspath(__file__)

import os
class MyClass(): pass
    self = MyClass()
myobj.path = os.path.abspath(__file__)
filepath = myobj.path
#The define code of myobj is:
```
```
"""
    result3 = \
"""
The define code of myobj is:
```
import os
class MyClass(): pass
    self = MyClass()
myobj.path = os.path.abspath(__file__)
```
"""
    exampe4 = \
"""
#based on the code:
class Toml:
def load(self, file_path):
    with open(self.file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=')
                self._set_nested_value(key.strip(), value.strip())

toml = Toml()

class Toml:
    def load(self, file_path):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    self._set_nested_value(key.strip(), value.strip())
toml = Toml()
data = toml.load(file)
#The define code of toml is:
```
```
"""
    result4 = \
"""
The define code of toml is:
```
class Toml:
    def load(self, file_path):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    self._set_nested_value(key.strip(), value.strip())
toml = Toml()
```
"""

    question = \
f"""
#based on the code:
{code}
#The define code of {entry['name']} is:
```
```
"""
    conversation.append({"role":"system", "content":"You can only reply with python code, all the explatation should be comment"})
    conversation.append({"role":"user", "content":exampe1})
    conversation.append({"role":"assistant", "content":result1})
    conversation.append({"role":"user", "content":exampe2})
    conversation.append({"role":"assistant", "content":result2})
    conversation.append({"role":"user", "content":exampe3})
    conversation.append({"role":"assistant", "content":result3})
    conversation.append({"role":"user", "content":exampe4})
    conversation.append({"role":"assistant", "content":result4})
    conversation.append({"role":"user", "content":question})
    return conversation