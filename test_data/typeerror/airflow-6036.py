for job in self._jobs:
    if job:
        self.log.info(
                    'Google Cloud DataFlow with job_id %s has name %s',
                    self._job_id, job['name']
                )