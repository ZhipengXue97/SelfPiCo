from ..predictor import Predictor
from ...Logging import logger
from ...IIDs import IIDs
from ..InputFactory import TypeInputFactory
from ...Hyperparams import Hyperparams as params
from ...ValueAbstraction import restore_value
import requests
import json
from .Prompt import GetPrompt




class CodeLLamaTypePredictor(Predictor):
    def __init__(self, stats):
        self.stats = stats
        self.iids = IIDs(params.iids_file)
        self.globle_module = []
        self.input_factory = TypeInputFactory(self.iids)
        self.entry = {}


    def _query_model(self, entry):

        def get(entry):
            conversation = GetPrompt(entry)
            response = requests.post(
                "http://localhost:5001/query", json=conversation)
            if response.status_code != 200:
                raise RuntimeError(
                    f"Model server returned error code {response.status_code}")
            return response
        
        self.entry = self.input_factory.entry_to_inputs(self.entry)
        response = get(entry)
        val_as_string = json.loads(response.text)["content"].strip()
        logger.info(val_as_string)
        val = restore_value(val_as_string)

        return val_as_string, val

        



    
    def name(self, iid, name):
        self.entry = {"iid": iid, "name": name, "kind": "name", "type": "type"}
        abstract_v, v = self._query_model(self.entry)
        logger.info(f"{iid}: Predicting for name {name}: {abstract_v}, {v}")
        self.stats.inject_value(
            iid, f"Inject {abstract_v} for variable {name}")
        return v

    def call(self, iid, fct, fct_name, *args, **kwargs):
        self.entry = {"iid": iid, "name": fct_name, "kind": "call", "type": "type"}
        abstract_v, v = self._query_model(self.entry)
        logger.info(f"{iid}: Predicting for call: {abstract_v}, {v}")
        self.stats.inject_value(
            iid, f"Inject {abstract_v} as return value of {fct_name}")
        return v
    

    def attribute(self, iid, base, attr_name):
        self.entry = {"iid": iid, "name": attr_name, "kind": "attribute", "type": "type"}
        abstract_v, v = self._query_model(self.entry)
        logger.info(f"{iid}: Predicting for attribute {attr_name}: {abstract_v}, {v}")
        self.stats.inject_value(
            iid, f"Inject {abstract_v} for attribute {attr_name}")
        return v
    
    
    