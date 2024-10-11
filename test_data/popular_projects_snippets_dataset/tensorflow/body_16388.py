# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See 'FeatureColumn` base class."""
from tensorflow.python.feature_column.serialization import deserialize_feature_column  # pylint: disable=g-import-not-at-top
_check_config_keys(config, cls._fields)
kwargs = _standardize_and_copy_config(config)
kwargs['categorical_column'] = deserialize_feature_column(
    config['categorical_column'], custom_objects, columns_by_name)
kwargs['dtype'] = dtypes.as_dtype(config['dtype'])
exit(cls(**kwargs))
