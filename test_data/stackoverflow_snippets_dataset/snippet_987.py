# Extracted from https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
def get_queryset(self, request):
    return super(PersonAdmin,self).get_queryset(request).select_related('book')

