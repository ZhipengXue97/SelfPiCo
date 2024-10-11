n_wo_defaults = len(spec.args) - len(spec.defaults)
defaults = ('',) * n_wo_defaults + spec.defaults