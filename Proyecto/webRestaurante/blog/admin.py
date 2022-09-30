from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    ordering = ('author','published')
    search_fields = ('title','author_username',)
    
    date_hierarchy = 'published'
    list_filter = ('author__first_name', 'categories__name')
    list_display = ('title','get_nombre','published', 'post_categories')
    
    def post_categories(self,obj):
        res = ""
        for c in obj.categories.all().order_by("name"):
            res += c.name + ", "
        res = res[0:len(res)-2]
        return res
    post_categories.short_description = "Categorias"
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

