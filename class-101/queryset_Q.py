# queryset_Q.py
from django.db.models import F
import datetime

from articles.models import Article, Tag

from django.db.models import Q

# OR 조건 (title에 'Django'가 포함되거나 content에 'ORM'이 포함)
articles = Article.objects.filter(
    Q(title__icontains='Django') | Q(content__icontains='ORM')
)

# AND 조건 (title에 'Django'가 포함되고 is_published가 True)
articles = Article.objects.filter(
    Q(title__icontains='Django') & Q(is_published=True)
)

# NOT 조건 (author가 'admin'이 아닌 게시글)
articles = Article.objects.filter(~Q(author__username='admin'))

# 복잡한 조합
articles = Article.objects.filter(
    (Q(title__icontains='Django') | Q(title__icontains='Python')) &
    Q(created__year=2025) &
    ~Q(author__username='admin')
)