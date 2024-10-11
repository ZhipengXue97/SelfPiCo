if get_logs:
    read_logs_since_sec = None
    last_log_time = None

delta = pendulum.now() - last_log_time
read_logs_since_sec = math.ceil(delta.total_seconds())