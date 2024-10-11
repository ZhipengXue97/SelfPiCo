# Extracted from https://stackoverflow.com/questions/1894269/how-to-convert-string-representation-of-list-to-a-list
import ast
l = ast.literal_eval('[ "A","B","C" , " D"]')
l = [i.strip() for i in l]

