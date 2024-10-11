try:
    current = math.floor(int(current_level * 100))
except ZeroDivisionError:
    current = 0