from ..predictor import Predictor
from ...Logging import logger
from ...IIDs import IIDs
from ..InputFactory import ValueInputFactory
from ...Util import exec_predict, remove_comments, check_import, remove_indentation
from ...Hyperparams import Hyperparams as params
from ...ValueAbstraction import restore_value
import requests
import json
import re
import openai
from .Prompt import GetPrompt, get_clean_conversation




class GptTypePredictor(Predictor):
    def __init__(self, stats):
        self.stats = stats
        self.api_key = ''
        self.iids = IIDs(params.iids_file)
        self.globle_module = []
        self.input_factory = ValueInputFactory(self.iids)


    def type_query_model(self, entry):
        def get(entry):
            conversation = GetPrompt(entry)
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages = conversation, temperature=0, max_tokens=5,  top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0)
            return response['choices'][0]['message']['content']

        def check_response(response):
            response = response.split("\n")
            for line in response:
                if "import " in line:
                    if check_import(line):
                        if line not in self.globle_module:
                            self.globle_module.append(line)

        def LLM_clean(code):
            code = remove_comments(code)
            conversation = get_clean_conversation(self.entry, code)
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages = conversation, temperature=0, max_tokens=5,  top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0)
            response = json.loads(response.text)["content"]
            pattern = r"```([\s\S]*?)```"
            response = re.search(pattern, response).group(1)
            response = remove_comments(response)
            response = remove_indentation(response)
            logger.info(f"{response}")
            return response
        
        def text_clean(code):
            code = remove_comments(code)
            code = remove_indentation(code)
            codelist = []
            code_lines = code.split("\n")
            for code_line in code_lines:
                if self.entry['target_line'] not in code_line and code_line not in codelist:
                    codelist.append(code_line)
            code = "\n".join(codelist)
            logger.info(f"{code}")
            return code


        

        def get_response():

            if self.entry['kind'] == "name":
                for i in range(3):
                    response = get(self.entry)
                    check_response(response)
                    try:
                        response = text_clean(response)
                        response = '\n'.join(self.globle_module) + response
                        v, _ = exec_predict(self.entry['name'], response)
                        return v, response
                    except:
                        try:
                            response = LLM_clean(response)
                            response = '\n'.join(self.globle_module) + response
                            v, _ = exec_predict(self.entry['name'], response)
                            return v, response
                        except Exception as ex:
                            e = str(ex)
                            self.entry['execute_error'] = e
                            self.entry['wrong_answer'] = response
                            logger.info(f"{e}")
                            continue
            

            if self.entry['kind'] == "attribute":
                for i in range(3):
                    response = get(self.entry)
                    check_response(response)
                    try:
                        response = text_clean(response)
                        response = '\n'.join(self.globle_module) + response
                        v, _ = exec_predict(self.entry['name'], response)
                        return getattr(v, self.entry['attr']), response
                    except:
                        try:
                            response = LLM_clean(response)
                            response = '\n'.join(self.globle_module) + response
                            v, _ = exec_predict(self.entry['name'], response)
                            return getattr(v, self.entry['attr']), response
                        except Exception as ex:
                            e = str(ex)
                            self.entry['execute_error'] = e
                            self.entry['wrong_answer'] = response
                            logger.info(f"{e}")
                            continue


            if self.entry['kind'] == "call":
                for i in range(3):
                    response = get(self.entry)
                    check_response(response)
                    try:
                        response = text_clean(response)
                        response = '\n'.join(self.globle_module) + response
                        v, _ = exec_predict(self.entry['name'], response)
                        return v, response
                    except:
                        try:
                            response = LLM_clean(response)
                            response = '\n'.join(self.globle_module) + response
                            v, _ = exec_predict(self.entry['name'], response)
                            return v, response
                        except Exception as ex:
                            e = str(ex)
                            self.entry['execute_error'] = e
                            self.entry['wrong_answer'] = response
                            logger.info(f"{e}")
                            continue
        
        self.entry = self.input_factory.entry_to_inputs(self.entry, self.env)
        v, response = get_response()

        return v, response
            

    

    def name(self, iid, name, e):
        self.entry = {"iid": iid, "name": name, "kind": "name", "type": "value", \
                 "orig_error":e, "execute_error":"", "wrong_answer" : ""}
        v, response = self._query_model()
        response = remove_comments(response)
        self.env[f"name#{name}"] = response
        logger.info(f"{iid}: Predicting for name {name}: {response}")
        self.stats.inject_value(
            iid, f"Inject value for variable {name}")
        return v

    def attribute(self, iid, baseclass, attr_name, e):
        self.entry = {"iid": iid, "baseclass": baseclass, "kind": "attribute", "attr":attr_name, \
                 "type": "value", "orig_error":e, "execute_error":"", "wrong_answer" : ""}
        v, response = self._query_model()
        response = remove_comments(response)
        self.env[f"name#{self.entry['name']}"] = response
        logger.info(f"{iid}: Updating for name {self.entry['name']}: {response}")
        self.stats.inject_value(
            iid, f"Updating value of {self.entry['name']}")
        return v, self.entry['name']

    def call(self, iid, fct, fct_name, e, *args, **kwargs):
        self.entry = {"iid": iid, "name": fct_name, "kind": "call", "type": "value", "orig_error":e, "wrong_answer" : "", "execute_error":""}
        response = self._query_model()
        logger.info(f"{iid}: Predicting for call {self.entry['name']}: {response}")
        self.stats.inject_value(
            iid, f"Inject value as return value of {fct_name}")
        return response

