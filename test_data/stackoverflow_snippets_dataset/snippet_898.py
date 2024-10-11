# Extracted from https://stackoverflow.com/questions/11029717/how-do-i-disable-log-messages-from-the-requests-library
import logging
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)

