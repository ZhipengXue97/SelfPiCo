# Extracted from https://stackoverflow.com/questions/26886653/create-new-column-based-on-values-from-other-columns-apply-a-function-of-multi
def as_hex(value):
    # clamp to avoid rounding errors etc.
    return min(max(0, int(value * 256)), 255)

def hex_color(row):
    r, g, b = as_hex(row['red']), as_hex(row['green']), as_hex(row['blue'])
    return f'#{r:02x}{g:02x}{b:02x}'

df['hex_color'] = df.apply(hex_color, axis=1)

def additive_color(row):
    # Insert here: logic that takes values from the `row` and computes
    # the desired cell value for the new column in that row.
    # The `row` is an ordinary `Series` object representing a row of the
    # original `DataFrame`; it can be indexed with column names, thus:
    if row['red'] > 0.5:
        if row['green'] > 0.5:
            return 'white' if row['blue'] > 0.5 else 'yellow'
        else:
            return 'magenta' if row['blue'] > 0.5 else 'red'
    elif row['green'] > 0.5:
        return 'cyan' if row['blue'] > 0.5 else 'green'
    else:
        return 'blue' if row['blue'] > 0.5 else 'black'

black = (df['red'] <= 0.5) & (df['green'] <= 0.5) & (df['blue'] <= 0.5)
white = (df['red'] > 0.5) & (df['green'] > 0.5) & (df['blue'] > 0.5)

df['color'] = np.select(
    [white, black],
    ['white', 'black'],
    'colorful'
)

df['color'] = 'colorful'
df.loc[white, 'color'] = 'white'
df.loc[black, 'color'] = 'black'

df['color'] = 'colorful'
df['color'] = df['color'].where(~white, 'white').where(~black, 'black')

def brightness(row):
    return row['red'] * .299 + row['green'] * .587 + row['blue'] * .114

df['brightness'] = df.apply(brightness, axis=1)

df['brightness'] = df['red'] * .299 + df['green'] * .587 + df['blue'] * .114

def as_hex(column):
    scaled = (column * 256).astype(int)
    clamped = scaled.where(scaled >= 0, 0).where(scaled <= 255, 255)
    return clamped.apply(lambda i: f'{i:02x}')

df['hex_color'] = '#' + as_hex(df['red']) + as_hex(df['green']) + as_hex(df['blue'])

