# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py
model_path = resource_loader.get_path_to_datafile(
    '../testdata/multi_add_flex.bin')
mock_stdout = io.StringIO()
with test.mock.patch.object(sys, 'stdout', mock_stdout):
    analyzer.ModelAnalyzer.analyze(
        model_path=model_path, gpu_compatibility=True)
txt = mock_stdout.getvalue()
self.assertIn(
    'GPU COMPATIBILITY WARNING: Not supported custom op FlexAddV2', txt)
self.assertIn(
    'GPU COMPATIBILITY WARNING: Subgraph#0 has GPU delegate compatibility '
    'issues at nodes 0, 1, 2', txt)
