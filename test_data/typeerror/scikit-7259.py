if self.anisotropic:
    return "{0}(length_scale=[{1}])".format(
        self.__class__.__name__, ", ".join(map("{0:.3g}".format,
                                            self.length_scale)))
else:  # isotropic
    return "{0}(length_scale={1:.3g})".format(
        self.__class__.__name__, self.length_scale)