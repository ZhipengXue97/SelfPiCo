# Extracted from https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
import logging
import sys


def create_stream_handler(stream, formatter, level, message_filter=None):
    handler = logging.StreamHandler(stream=stream)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    if message_filter:
        handler.addFilter(message_filter)
    return handler


def configure_logger(logger: logging.Logger, enable_console: bool = True, enable_file: bool = True):
    if not logger.handlers:
        if enable_console:
            message_format: str = '{asctime:20} {name:16} {levelname:8} {message}'
            date_format: str = '%Y/%m/%d %H:%M:%S'
            level: int = logging.DEBUG
            formatter = logging.Formatter(message_format, date_format, '{')

            # Configures error output (from Warning levels).
            error_output_handler = create_stream_handler(sys.stderr, formatter,
                                                         max(level, logging.WARNING))
            logger.addHandler(error_output_handler)

            # Configures standard output (from configured Level, if lower than Warning,
            #  and excluding everything from Warning and higher).
            if level < logging.WARNING:
                standard_output_filter = lambda record: record.levelno < logging.WARNING
                standard_output_handler = create_stream_handler(sys.stdout, formatter, level,
                                                                standard_output_filter)
                logger.addHandler(standard_output_handler)

        if enable_file:
            message_format: str = '{asctime:20} {name:16} {levelname:8} {message}'
            date_format: str = '%Y/%m/%d %H:%M:%S'
            level: int = logging.DEBUG
            output_file: str = '/tmp/so_test.log'

            handler = logging.FileHandler(output_file)
            formatter = logging.Formatter(message_format, date_format, '{')
            handler.setLevel(level)
            handler.setFormatter(formatter)
            logger.addHandler(handler)

logger: logging.Logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)
configure_logger(logger, True, True)
logger.debug('Debug message ...')
logger.info('Info message ...')
logger.warning('Warning ...')
logger.error('Error ...')
logger.fatal('Fatal message ...')

