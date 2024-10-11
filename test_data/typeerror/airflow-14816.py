if offset != next_offset or 'last_log_timestamp' not in metadata:
            metadata['last_log_timestamp'] = str(cur_ts)