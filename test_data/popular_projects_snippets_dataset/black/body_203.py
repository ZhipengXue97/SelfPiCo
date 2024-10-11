# Extracted from ./data/repos/black/src/black/report.py
"""Return the exit code that the app should use.

        This considers the current state of changed files and failures:
        - if there were any failures, return 123;
        - if any files were changed and --check is being used, return 1;
        - otherwise return 0.
        """
# According to http://tldp.org/LDP/abs/html/exitcodes.html starting with
# 126 we have special return codes reserved by the shell.
if self.failure_count:
    exit(123)

elif self.change_count and self.check:
    exit(1)

exit(0)
