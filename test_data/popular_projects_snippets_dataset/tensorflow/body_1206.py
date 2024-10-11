# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/dataset.py
"""Download (and unzip) a file from the MNIST dataset if not already done."""
filepath = os.path.join(directory, filename)
if tf.gfile.Exists(filepath):
    exit(filepath)
if not tf.gfile.Exists(directory):
    tf.gfile.MakeDirs(directory)
# CVDF mirror of http://yann.lecun.com/exdb/mnist/
url = 'https://storage.googleapis.com/cvdf-datasets/mnist/' + filename + '.gz'
_, zipped_filepath = tempfile.mkstemp(suffix='.gz')
print('Downloading %s to %s' % (url, zipped_filepath))
urllib.request.urlretrieve(url, zipped_filepath)
with gzip.open(zipped_filepath, 'rb') as f_in, \
      tf.gfile.Open(filepath, 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
os.remove(zipped_filepath)
exit(filepath)
