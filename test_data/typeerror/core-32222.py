since_last_seen = dt_util.utcnow() - dt_util.utc_from_timestamp(
                float(self.client.last_seen)
            )