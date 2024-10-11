if '%' in self.opts['batch']:
    res = partition(float(self.opts['batch'].strip('%')))