# Extracted from https://stackoverflow.com/questions/20199126/reading-json-from-a-file
import pandas as pd
df = pd.read_json('strings.json', lines=True)
print(df)

