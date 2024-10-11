# Extracted from https://stackoverflow.com/questions/1074212/how-to-see-the-raw-sql-queries-django-is-running
from django.db import connection
print(connection.queries)

print(MyModel.objects.filter(name="my name").query)

from django.db import reset_queries
from django.db import connection

reset_queries()
# Run your query here
print(connection.queries)
[]

