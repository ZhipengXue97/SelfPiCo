# Extracted from https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
def test_afunction_throws_exception(self):
    self.assertRaises(ExpectedException, afunction)

def test_afunction_throws_exception(self):
    self.assertRaises(ExpectedException, afunction, arg1, arg2)

