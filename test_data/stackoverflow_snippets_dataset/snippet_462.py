# Extracted from https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def is_string_convertable_to_int(value: str) -> bool:
    return value.replace('-', '').isdigit()

