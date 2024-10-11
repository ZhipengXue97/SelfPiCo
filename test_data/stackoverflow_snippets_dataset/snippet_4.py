# Extracted from https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

