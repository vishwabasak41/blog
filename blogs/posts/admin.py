from django.contrib import admin

# Register your models here.
from posts.models import(Post)


class ADMINPOST(admin.ModelAdmin):
	list_display=["__unicode__","timestamp"]
	class Meta:
		model=Post

admin.site.register(Post,ADMINPOST)