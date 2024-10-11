# Extracted from https://stackoverflow.com/questions/629551/how-to-query-as-group-by-in-django
dupes_query = MyModel.objects.all().values('my_field').annotate(
    count=Count('id')
).order_by('-count').filter(count__gt=1)

