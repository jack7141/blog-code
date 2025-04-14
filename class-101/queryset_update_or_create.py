# queryset_update_or_create.py
from articles.models import Article, Tag

# update_or_create() - 있으면 업데이트, 없으면 생성
article, created = Article.objects.update_or_create(
    id="ada7a1826ce74be3b3585cf3ea13bb00",  # 조회 조건
    defaults={                  # 생성 또는 업데이트할 필드
        'title': '업데이트된 내용입니다.',
        'is_published': True
    }
)
print(f"Article '{article.title}'는 {'새로 생성됨' if created else '이미 존재함'}")