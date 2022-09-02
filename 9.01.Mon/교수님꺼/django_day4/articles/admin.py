from django.contrib import admin
from .models import Article

# 가장 기본적으로 추가하는 방법
# admin.site.register(Article)

# 응용편
class ArticleAdmin(admin.ModelAdmin):
    # admin 사이트 목록에 보였으면 하는 데이터 리스트
    list_display = ['id', 'title', 'updated_at']

    # 그 중 클릭이 가능하도록 설정하고 싶은 리스트
    list_display_links = ['id', 'title']
    

# 모델과 커스터마이징한 admin class 를 등록
admin.site.register(Article, ArticleAdmin)