# queryset_annotate_aggreate.py
from django.db.models import Count, Sum, Avg, Max
from articles.models import Article, Tag
from django.db.models.functions import TruncMonth

from users.models import User

# aggregate() - 전체 QuerySet에 대한 집계 결과를 딕셔너리로 반환
result = Article.objects.aggregate(
    total_articles=Count('id'),
    avg_likes=Avg('likes_count'),
    max_comments=Max('comments_count')
)
print(result)

# annotate() - 각 객체에 집계 필드를 추가하여 QuerySet 반환
authors_with_stats = User.objects.annotate(
    articles_count=Count('article'),
    total_likes=Sum('article__likes_count')
).order_by('-total_likes')[:5]

for author in authors_with_stats:
    print(f"{author.username}: 게시글 {author.articles_count}개, 좋아요 {author.total_likes}개")

# 그룹화와 함께 사용
# 태그별 게시글 수 계산
tags_with_counts = Tag.objects.annotate(
    articles_count=Count('article')
).order_by('-articles_count')

# 날짜별 집계
# 월별 게시글 작성 통계
monthly_stats = Article.objects.annotate(
    month=TruncMonth('created')
).values('month').annotate(
    count=Count('id')
).order_by('month')