# Extracted from https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
class MyModel(models.Model):

    check_in = models.DateField()

    class Meta:
        ordering = ('-check_in',)

