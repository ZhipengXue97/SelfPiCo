# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
temp_dir = tempfile.mkdtemp()
config = server_lib.DispatcherConfig(
    work_dir=temp_dir, fault_tolerant_mode=True)
dispatcher = server_lib.DispatchServer(  # pylint: disable=unused-variable
    config=config, start=True)
