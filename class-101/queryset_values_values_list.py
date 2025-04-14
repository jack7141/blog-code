# queryset_values_values_list.py
from articles.models import Article

# values() - 딕셔너리 형태로 반환
articles_dict = Article.objects.values('id', 'title', 'author__username')
print(articles_dict)

# values_list() - 튜플 형태로 반환
articles_tuple = Article.objects.values_list('id', 'title')
print(articles_tuple)

# flat=True 옵션으로 단일 필드만 리스트로 받기
article_titles = Article.objects.values_list('title', flat=True)
print(article_titles)