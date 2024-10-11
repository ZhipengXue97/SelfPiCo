# Extracted from https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options
import warnings

# Force mixed datatype warning to be a python error so we can catch it and reattempt the 
# load using the slower python engine
warnings.simplefilter('error', pandas.errors.DtypeWarning)
try:
    df = pandas.read_csv(path, sep=sep, encoding=encoding)
except pandas.errors.DtypeWarning:
    df = pandas.read_csv(path, sep=sep, encoding=encoding, engine="python")

