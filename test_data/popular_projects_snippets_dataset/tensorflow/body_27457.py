# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
if model._distribution_strategy:
    for mode in [ModeKeys.TRAIN, ModeKeys.TEST, ModeKeys.PREDICT]:
        distributed_model = get_distributed_model(model, mode)
        if distributed_model:
            first_model = model._distribution_strategy.unwrap(distributed_model)[0]
            first_model.reset_metrics()
