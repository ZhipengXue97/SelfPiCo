# Extracted from https://stackoverflow.com/questions/855759/what-is-the-intended-use-of-the-optional-else-clause-of-the-try-statement-in
try:
    data = something_that_can_go_wrong()
except Exception as e: # yes, I know that's a bad way to do it...
    handle_exception(e)
else:
    do_stuff(data)
finally:
    clean_up()

