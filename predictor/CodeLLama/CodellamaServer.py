import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
import torch
import transformers
from flask import Flask, json, request
from transformers import AutoTokenizer
from ...Logging import logger
import logging


class ModelServer:
    def __init__(self, model, port):
        self.port = port
        self.model = model
        self._initialize_model()
        self._initialize_http_server()

    def _initialize_model(self):
        logger.info("Loading Codellama model")

        self.pipeline = transformers.pipeline(
            "conversational",
            model=self.model,
            torch_dtype=torch.float16,
            do_sample=True,
            device_map="auto",
        )
        logger.info("Codellama value model loaded")

        

    def _initialize_http_server(self):
        api = Flask(__name__)
        flask_log = logging.getLogger('werkzeug')
        flask_log.setLevel(logging.ERROR)
        @api.route('/query', methods=['POST'])
        def handle_query():
            conversation = request.json
            response = self.pipeline(conversation, temperature = 0.01)

            return response[-1]
        
        api.run(port=self.port)

if __name__ == "__main__":
    ModelServer("codellama/snapshots/codellama-sft/checkpoint-450", "5001")

#python -m SelfDyCo.predictor.CodeLLama.CodellamaServer