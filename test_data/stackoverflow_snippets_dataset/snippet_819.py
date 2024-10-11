# Extracted from https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models
SomeModel.objects.get(pk=1).delete()
# Or
SomeModel.objects.filter(pk=1).delete()

# SQL equivalent
# delete from table_name where id = 1;

SomeModel.objects.fitler(pk__in=[1,2,3,4,5,...]).delete()

# SQL equivalent
# delete from table_name where id in (1,2,4,5,...);

SomeModel.objects.all().delete()

# SQL equivalent
# delete from table_name;

