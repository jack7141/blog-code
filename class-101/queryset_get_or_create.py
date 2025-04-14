# queryset_get_or_create.py
from articles.models import Article, Tag

#  get_or_create() - 있으면 가져오고, 없으면 생성
tag, created = Tag.objects.get_or_create(name='FastAPI')
print(f"태그 '{tag.name}'는 {'새로 생성됨' if created else '이미 존재함'}")
