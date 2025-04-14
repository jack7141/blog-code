# 모든 게시글 조회
from articles.models import Article

all_articles = Article.objects.all()

# 조건으로 필터링
published_articles = Article.objects.filter(is_published=True)

# 특정 ID로 단일 객체 가져오기
try:
    first_article = Article.objects.get(id='ada7a1826ce74be3b3585cf3ea13bb00')
    print(f"ID가 1인 게시글 제목: {first_article.title}")
except Article.DoesNotExist:
    print("ID가 1인 게시글이 없습니다.")