from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
# fields = ['name', 'title', 'contents', 'url', 'email', 'owner'] 
    fieldsets = [
        ('제목' , {'fields': ['title']}), 
        ('내용', {'fields':['contents']}),
        ('작성자 정보', {'fields':['name', 'url', 'email', 'owner']}), 
    ]
# admin 페이지에 Article 데이터 모델 등록
admin.site.register(Article, ArticleAdmin)