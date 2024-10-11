# Extracted from https://stackoverflow.com/questions/427102/what-is-a-slug-in-django
prepopulated_fields = {'slug': ('title', )}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('content', )

    prepopulated_fields = {'slug': ('title', )}

