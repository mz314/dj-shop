from django.contrib import admin
from cms.models import *

class ArticleAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)


