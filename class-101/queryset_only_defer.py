# queryset_only_defer.py
from articles.models import Article, Tag

# only() - 특정 필드만 가져오기
# 실제 SQL: SELECT id, title, created FROM articles
articles_only_title = Article.objects.only('title', 'created')
for article in articles_only_title:
    print(f"특정 필드만 가져오기: article created: {article.created}, article title: {article.title}")

# defer() - 특정 필드 제외하고 가져오기
# 실제 SQL: SELECT id, title, created, author_id, ... FROM articles (content 필드 제외)
articles_defer_content = Article.objects.defer('content')
print(articles_defer_content.values())