from django.db import models

# Create your models here.
# 엑셀에 비유하면 이해가 쉽다 !
# Article = 테이블명 = Sheet 이름
# title, content, ... = column 이름
# models.~~ = 데이터 정의
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Article 클래스 호출 시 어떻게 출력할 것인가 ?
    def __str__(self):
        return f'{self.title}'