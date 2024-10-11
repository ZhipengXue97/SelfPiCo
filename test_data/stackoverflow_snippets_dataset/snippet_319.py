# Extracted from https://stackoverflow.com/questions/5214578/print-string-to-text-file
with open('Output.txt', 'w', encoding='utf-8') as f:
    f.write(f'Purchase Amount: {TotalAmount}')

