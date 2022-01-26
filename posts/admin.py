from django.contrib import admin
from .models import Post,Category,Profile,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','title_tag','description','post_date','category','snippet')
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','bio','website_url','facebook_url','twitter_url','instagram_url','linkedin_url')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','description','date_added')

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Comment,CommentAdmin)
