# Extracted from https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering
results = Model.objects.filter(x=5).exclude(a=true)

