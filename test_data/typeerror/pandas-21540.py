if record_prefix is not None:
        result.rename(columns=lambda x: record_prefix + x, inplace=True)