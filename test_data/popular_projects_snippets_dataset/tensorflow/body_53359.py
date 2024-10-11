# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
# A first call using the non-delayed pipeline. The batcher will send an
# empty tensor along the non-delayed pipeline.
thread_results.extend(sess.run([result], feed_dict={inp: [1]}))
