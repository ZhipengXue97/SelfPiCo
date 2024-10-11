# Extracted from https://stackoverflow.com/questions/12151306/argparse-way-to-include-default-values-in-help
class ExplicitDefaultsHelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def _get_help_string(self, action):
        if action.default in (None, False):
            return action.help
        return super()._get_help_string(action)

parser = argparse.ArgumentParser(
        formatter_class=ExplicitDefaultsHelpFormatter
                )

