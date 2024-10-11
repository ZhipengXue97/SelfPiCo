# Extracted from https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
import io
my_string = "hi there"

with io.open("output_file.txt", mode='w', encoding='utf-8') as f:
    f.write(my_string)

