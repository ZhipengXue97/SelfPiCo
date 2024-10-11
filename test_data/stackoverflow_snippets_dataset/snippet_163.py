# Extracted from https://stackoverflow.com/questions/3702675/how-to-catch-and-print-the-full-exception-traceback-without-halting-exiting-the
import io
import traceback

try:
    call_code_that_fails()
except:

    errors = io.StringIO()
    traceback.print_exc(file=errors)  # Instead of printing directly to stdout, the result can be further processed
    contents = str(errors.getvalue())
    print(contents)
    errors.close()

