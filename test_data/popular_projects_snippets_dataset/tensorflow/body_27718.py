# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
super(Adam, self).__init__(**kwargs)
with backend.name_scope(self.__class__.__name__):
    self.iterations = backend.variable(0, dtype='int64', name='iterations')
    self.lr = backend.variable(lr, name='lr')
    self.beta_1 = backend.variable(beta_1, name='beta_1')
    self.beta_2 = backend.variable(beta_2, name='beta_2')
    self.decay = backend.variable(decay, name='decay')
if epsilon is None:
    epsilon = backend.epsilon()
self.epsilon = epsilon
self.initial_decay = decay
self.amsgrad = amsgrad
