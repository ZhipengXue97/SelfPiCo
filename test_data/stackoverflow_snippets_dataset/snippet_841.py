# Extracted from https://stackoverflow.com/questions/5029934/defaultdict-of-defaultdict
for x in stuff:
    d[x.a][x.b] += x.c_int

d = defaultdict(int)
for x in stuff:
    d[x.a,x.b] += x.c_int
    # ^^^^^^^ tuple key

