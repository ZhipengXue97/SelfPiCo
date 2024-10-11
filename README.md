# SelfPiCo: Self-Guided Partial Code Execution with LLMs (ISSTA'24)

## How to use
### Step 0: Before we start
This project is developed based [Lexecutor](https://github.com/michaelpradel/LExecutor/tree/main), so we strongly recommend to read the document of Lexecutor first.

## SelfPiCo-GPT
### Step 1: Instrument the partial code snippet
`python -m SelfDyCo.Instrument --files test.py --iids iids.json`

### Step 2: Set the mode
1. change the base LLM in `Runtime.py`
2. Using your own Openai API key in `SelfPiCo/pedictor/GPT/ValuePrediector.py` and `SelfPiCo/pedictor/GPT/TypePrediector.py`

### Step 3: Guide partial code execution
Direct execute the instrumented partial code

## SelfPiCo-CodeLlama
### Step 1: Instrument the partial code snippet
`python -m SelfDyCo.Instrument --files test.py --iids iids.json`

### Step 2: Fine-tune the CodeLLama model
1. Collect the variable type data by [Lexecutor](https://github.com/michaelpradel/LExecutor/tree/main)
2. Running SelfPiCo/pedictor/CodeLLama/PrepareData.py 
3. Running SelfPiCo/pedictor/CodeLLama/FineTune.py 

### Step 3: Guide partial code execution
1. start up the model
`python -m SelfDyCo.predictor.CodeLLama.CodellamaServer`
2. Direct execute the instrumented partial code
