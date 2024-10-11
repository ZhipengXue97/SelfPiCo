from abc import ABC


class Predictor(ABC):
    def name(self, iid, name):
        pass

    def call(self, iid, fct, fct_name, *args, **kwargs):
        pass

    def attribute(self, iid, base, attr_name):
        pass

    def binary_operation(self, iid, left, operator, right):
        pass
