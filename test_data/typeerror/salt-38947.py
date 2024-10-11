self.ssh_options = ssh_options
return ' '.join(['-o {0}'.format(opt)
                        for opt in self.ssh_options])