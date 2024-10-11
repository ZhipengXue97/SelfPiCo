# Extracted from https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
memoryview(b"some bytes").tolist()

[115, 111, 109, 101, 32, 98, 121, 116, 101, 115]

memoryview(bytes("\u0075\u006e\u0069\u0063\u006f\u0064\u0065\u0020", "UTF-16")).tolist()

[255, 254, 117, 0, 110, 0, 105, 0, 99, 0, 111, 0, 100, 0, 101, 0, 32, 0]

#Another way to do the same
memoryview("\u0075\u006e\u0069\u0063\u006f\u0064\u0065\u0020".encode("UTF-16")).tolist()

[255, 254, 117, 0, 110, 0, 105, 0, 99, 0, 111, 0, 100, 0, 101, 0, 32, 0]

memoryview(bytes("\u0075\u006e\u0069\u0063\u006f\u0064\u0065\u0020", "UTF-16")).cast("H").tolist()

[65279, 117, 110, 105, 99, 111, 100, 101, 32]

memoryview(b"some  more  data").cast("L").tolist()

[1701670771, 1869422624, 538994034, 1635017060]


txt = "\u0075\u006e\u0069\u0063\u006f\u0064\u0065\u0020"
for order in ("", "BE", "LE"):
    mv = memoryview(bytes(txt, f"UTF-16{order}"))
    print(mv.cast("H").tolist())

[65279, 117, 110, 105, 99, 111, 100, 101, 32]
[29952, 28160, 26880, 25344, 28416, 25600, 25856, 8192]
[117, 110, 105, 99, 111, 100, 101, 32]

