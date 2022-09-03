from django.db import models

# Create your models here.
# Article = 테이블명
class Article(models.Model):
    title =  models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # timezone.now()
    updated_at = models.DateTimeField(auto_now=True)



# 구조 설명서 == blueprint(models.py) -> 실제 설계도(migrations) -> 반영(migrate)


# Article 클래스 호출 시 어떻게 출력할 것인가
    def __str__(self):
        return f'{self.title} {self.content}'




