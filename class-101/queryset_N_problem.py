# queryset_N_problem.py
from articles.models import Article, Tag

# select_related: 1:1 또는 N:1 관계에서 사용 (JOIN 활용)
articles = Article.objects.select_related('author')
for article in articles:
    # 추가 쿼리 없이 author 정보에 접근 가능
    print(article.author.username)

# prefetch_related: M:N 또는 1:N 역참조 관계에서 사용 (별도 쿼리 + Python에서 결합)
articles = Article.objects.prefetch_related('tags')
for article in articles:
    # 추가 쿼리 없이 tags 정보에 접근 가능
    print([tag.name for tag in article.tags.all()])

# 중첩된 관계도 처리 가능
articles = Article.objects.select_related('author').prefetch_related(
    'tags', 'comments', 'comments__author'
)