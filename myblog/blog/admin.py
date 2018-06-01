from django.contrib import admin
from blog.models import BlogsPost

# Register your models here.

class BlogsPostAdmin(admin.ModelAdmin):
	list_display = ['title','body','timestemp']

admin.site.register(BlogsPost,BlogsPostAdmin)

# admin.site.register(Category)
# admin.site.register(Post)
# admin.site.register(Tag)
