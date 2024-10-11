# Extracted from https://stackoverflow.com/questions/123198/how-to-copy-files
with open('sourcefile', 'rb') as f, open('destfile', 'wb') as g:
    while True:
        block = f.read(16*1024*1024)  # work by blocks of 16 MB
        if not block:  # end of file
            break
        g.write(block)

