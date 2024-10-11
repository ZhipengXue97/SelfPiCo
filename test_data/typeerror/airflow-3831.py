path_components = file_name[self.GCS_PREFIX_LENGTH:].split('/')
if path_components < 2:
    raise Exception(
        'Invalid Google Cloud Storage (GCS) object path: {}.'
        .format(file_name))