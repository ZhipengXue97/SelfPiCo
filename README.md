#SelfPiCo: Self-Guided Partial Code Execution with LLMs

## How to use
### Step 0: Before we start
This project is developed based [Lexecutor](https://github.com/michaelpradel/LExecutor/tree/main), so we strongly recommend to read the document of Lexecutor first.

### Step 1: Fine-tune the CodeLLama model
1. Collect the variable type data by lexecutor
2. Runing SelfPiCo/pedictor/CodeLLama/PrepareData.py 
3. Runing SelfPiCo/pedictor/CodeLLama/FineTune.py 

### Step 2: Use the model to gudie partial code execution
1.Runing SelfPiCo/Instrument.py to instrument the partial code
2. start up the model
For CodeLLama, Runing SelfPiCo/pedictor/CodeLLama/CodeLLamaServer.py to start the codellama model server
For GPT-3.5, useing your own openai API key in SelfPiCo/pedictor/GPT/ValuePrediector.py and SelfPiCo/pedictor/GPT/TypePrediector.py
3. Direct execut the instrumented partial code
