# queryset_exclude.py
from articles.models import Article

# 미발행 게시글 찾기
unpublished = Article.objects.exclude(is_published=True)
print(f"발행되지 않은 게시글 수: {unpublished.count()}")

# 특정 단어가 제목에 포함되지 않는 게시글
non_django = Article.objects.exclude(title__icontains='django')
print(f"제목에 'django'가 포함되지 않은 게시글 수: {non_django.count()}")

# 특정 작성자의 게시글 제외
non_admin = Article.objects.exclude(author__username='admin')
print(f"admin이 작성하지 않은 게시글 수: {non_admin.count()}")

# 여러 조건 제외하기
filtered_articles = Article.objects.exclude(
    title__icontains='django'
).exclude(
    author__username='admin'
)
print(f"제목에 'django'가 없고, admin이 작성하지 않은 게시글 수: {filtered_articles.count()}")