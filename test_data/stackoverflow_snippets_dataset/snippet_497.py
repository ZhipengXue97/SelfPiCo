# Extracted from https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
chunk_size = 4
for i in range(0, len(ints), chunk_size):
    chunk = ints[i:i+chunk_size]
    # process chunk of size <= chunk_size

