from django.contrib import admin


from .models import  Category, Tag, Post



class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'category', 'is_publish', 'author', 'publish_date')
    list_display_links=('id', 'title')
    list_filter=('category', 'author')
    list_editable=('is_publish',)
    search_fields=( 'title',  'description', 'content', )
   

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)


