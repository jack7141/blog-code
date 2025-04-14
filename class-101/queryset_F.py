# queryset_F.py
from django.db.models import F
import datetime

from articles.models import Article, Tag

# 조회 조건에서 F 표현식 사용
# likes가 comments보다 많은 게시글 찾기
popular_articles = Article.objects.filter(likes_count__gt=F('comments_count'))
for article in popular_articles:
    print(article.title)
# 업데이트에서 F 표현식 사용
# 조회수 증가
article_count = Article.objects.filter(id=1).update(views_count=F('views_count') + 1)
for article in article_count:
    print(article.views_count)
